#!/usr/bin/env python3
"""Sincroniza métricas de posts do Instagram (Meta Graph API) para o banco
"Posts" do Notion.

Ver documentação completa, pré-requisitos e limitações em
`docs/metricas-automacao.md`. Não editar este script sem ler aquele
documento primeiro — ele explica por que "Cliques no link" fica de fora,
por que o casamento é feito por permalink (não por ID salvo em algum
lugar), e por que não há renovação automática de token.

Variáveis de ambiente obrigatórias:
    META_ACCESS_TOKEN            token de longa duração da Graph API
    META_IG_BUSINESS_ID          Instagram Business Account ID
    NOTION_API_KEY               token de integração interna do Notion
    NOTION_POSTS_DATA_SOURCE_ID  id do data source "Posts" (sem prefixo collection://)

Só usa a biblioteca padrão do Python (urllib) — de propósito, para não
exigir passo de `pip install` no workflow do GitHub Actions.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

GRAPH_API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"
NOTION_API_BASE = "https://api.notion.com/v1"
# 2025-09-03+ é a versão da API que trata "data source" como objeto de
# primeira classe (necessário para /v1/data_sources/{id}/query, já que
# "Posts" é um database multi-source — ver docs/notion.md). Uma versão
# anterior não reconhece esse endpoint.
NOTION_VERSION = "2025-09-03"

# Posts publicados há mais que isso não são revisitados a cada rodada —
# a métrica já estabilizou (ver docs/metricas-automacao.md).
JANELA_DIAS = 45

# Nomes de métrica tentados em ordem, por incompatibilidade de mídia
# (Reels/vídeo vs. imagem/carrossel) e por mudança de nomenclatura entre
# versões da Graph API. O primeiro que responder sem erro é usado.
METRICAS_INSIGHTS = {
    "Alcance": ["reach", "impressions"],
    "Salvamentos": ["saved"],
    "Compartilhamentos": ["shares"],
}


class ErroConfiguracao(RuntimeError):
    pass


def _env(nome: str) -> str:
    valor = os.environ.get(nome, "").strip()
    if not valor:
        raise ErroConfiguracao(f"Variável de ambiente obrigatória ausente: {nome}")
    return valor


def _http_json(url: str, method: str = "GET", headers: dict | None = None, body: dict | None = None) -> dict:
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detalhe = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} em {method} {url}: {detalhe}") from exc


def graph_get(path: str, params: dict, token: str) -> dict:
    params = {**params, "access_token": token}
    url = f"{GRAPH_API_BASE}/{path}?{urllib.parse.urlencode(params)}"
    return _http_json(url)


def notion_headers(notion_key: str) -> dict:
    return {
        "Authorization": f"Bearer {notion_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def buscar_posts_instagram_pendentes(data_source_id: str, notion_key: str) -> list[dict]:
    """Posts de Instagram publicados, com link preenchido, dentro da janela
    de reavaliação. Usa a query API do Notion (filtro simples via REST
    clássico de databases, que continua funcionando sobre data sources)."""
    limite = (datetime.now(timezone.utc) - timedelta(days=JANELA_DIAS)).date().isoformat()
    # Nota: "Data" é o nome real da propriedade no schema do Notion (tipo
    # date). O alias "date:Data:start" só existe dentro do bridge SQL do
    # MCP do Notion (usado em sessões interativas do Claude Code) — a API
    # REST clássica usada aqui exige o nome e o tipo reais da propriedade.
    body = {
        "filter": {
            "and": [
                {"property": "Canal", "select": {"equals": "Instagram"}},
                {"property": "Status", "select": {"equals": "Publicado"}},
                {"property": "Link do post", "url": {"is_not_empty": True}},
                {"property": "Data", "date": {"on_or_after": limite}},
            ]
        },
        "page_size": 100,
    }
    resultados: list[dict] = []
    url = f"{NOTION_API_BASE}/data_sources/{data_source_id}/query"
    cursor = None
    while True:
        if cursor:
            body["start_cursor"] = cursor
        resposta = _http_json(url, method="POST", headers=notion_headers(notion_key), body=body)
        resultados.extend(resposta.get("results", []))
        if not resposta.get("has_more"):
            break
        cursor = resposta.get("next_cursor")
    return resultados


def listar_midias_recentes(ig_business_id: str, token: str, limite_paginas: int = 5) -> dict[str, str]:
    """Retorna {permalink: media_id} das mídias recentes da conta."""
    mapa: dict[str, str] = {}
    resposta = graph_get(
        f"{ig_business_id}/media",
        {"fields": "id,permalink", "limit": 100},
        token,
    )
    paginas = 0
    while True:
        for item in resposta.get("data", []):
            permalink = item.get("permalink")
            media_id = item.get("id")
            if permalink and media_id:
                mapa[permalink.rstrip("/")] = media_id
        proxima = resposta.get("paging", {}).get("next")
        paginas += 1
        if not proxima or paginas >= limite_paginas:
            break
        resposta = _http_json(proxima)
    return mapa


def buscar_metricas_midia(media_id: str, token: str) -> dict[str, int | None]:
    metricas: dict[str, int | None] = {}

    base = graph_get(media_id, {"fields": "like_count,comments_count"}, token)
    metricas["Curtidas"] = base.get("like_count")
    metricas["Comentários"] = base.get("comments_count")

    for campo_notion, nomes_possiveis in METRICAS_INSIGHTS.items():
        valor = None
        for nome in nomes_possiveis:
            try:
                insight = graph_get(f"{media_id}/insights", {"metric": nome}, token)
                dados = insight.get("data", [])
                if dados:
                    valores = dados[0].get("values", [])
                    if valores:
                        valor = valores[0].get("value")
                        break
            except RuntimeError:
                # métrica não suportada para este tipo de mídia — tenta a próxima
                continue
        metricas[campo_notion] = valor

    return metricas


def atualizar_pagina_notion(page_id: str, metricas: dict[str, int | None], notion_key: str) -> None:
    properties = {}
    for campo, valor in metricas.items():
        if valor is None:
            continue
        properties[campo] = {"number": valor}
    if not properties:
        return
    url = f"{NOTION_API_BASE}/pages/{page_id}"
    _http_json(url, method="PATCH", headers=notion_headers(notion_key), body={"properties": properties})


def main() -> int:
    try:
        meta_token = _env("META_ACCESS_TOKEN")
        ig_business_id = _env("META_IG_BUSINESS_ID")
        notion_key = _env("NOTION_API_KEY")
        data_source_id = _env("NOTION_POSTS_DATA_SOURCE_ID")
    except ErroConfiguracao as exc:
        print(f"Configuração incompleta: {exc}", file=sys.stderr)
        return 1

    print(f"Buscando posts de Instagram publicados nos últimos {JANELA_DIAS} dias...")
    posts = buscar_posts_instagram_pendentes(data_source_id, notion_key)
    print(f"{len(posts)} posts encontrados no Notion.")

    if not posts:
        print("Nada a sincronizar.")
        return 0

    print("Buscando mídias recentes da conta do Instagram...")
    midias_por_permalink = listar_midias_recentes(ig_business_id, meta_token)
    print(f"{len(midias_por_permalink)} mídias recentes retornadas pela API.")

    casados = 0
    atualizados = 0
    sem_correspondencia = 0

    for post in posts:
        props = post.get("properties", {})
        link = (props.get("Link do post") or {}).get("url")
        tema = "".join(
            t.get("plain_text", "")
            for t in (props.get("Tema") or {}).get("title", [])
        ) or post["id"]

        if not link:
            continue
        media_id = midias_por_permalink.get(link.rstrip("/"))
        if not media_id:
            sem_correspondencia += 1
            print(f"  [sem correspondência] {tema} ({link})")
            continue

        casados += 1
        try:
            metricas = buscar_metricas_midia(media_id, meta_token)
        except RuntimeError as exc:
            print(f"  [erro ao buscar métricas] {tema}: {exc}", file=sys.stderr)
            continue

        try:
            atualizar_pagina_notion(post["id"], metricas, notion_key)
            atualizados += 1
            print(f"  [atualizado] {tema}: {metricas}")
        except RuntimeError as exc:
            print(f"  [erro ao atualizar Notion] {tema}: {exc}", file=sys.stderr)

    print(
        f"\nResumo: {len(posts)} posts revisados, {casados} casados com mídia do "
        f"Instagram, {atualizados} atualizados, {sem_correspondencia} sem "
        f"correspondência (post publicado no Instagram fora da janela retornada "
        f"pela API, ou link do post não bate com o permalink exato)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
