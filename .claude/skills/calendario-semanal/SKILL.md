---
name: calendario-semanal
description: Gera dois calendários editoriais semanais separados — LinkedIn (3 posts) e Instagram (4 posts, um por área do direito, Cível cobrindo os subtemas Imobiliário/Família/Responsabilidade Civil/Direito das coisas/Contratos) — do escritório Gutmann & Silva, aplica o checklist de conformidade OAB, gera o relatório de métricas pendente, publica no Notion e comita em main. Use quando disparado pela Routine de quinta-feira ou quando pedirem para gerar/ensaiar o calendário de uma semana.
---

# Calendário editorial semanal — Gutmann & Silva

Procedimento completo. O prompt da Routine (`PROMPT_ROTINA.md`) é
deliberadamente curto porque toda a lógica vive aqui — mudanças de processo
devem ser feitas neste arquivo, não no prompt.

Desde 2026-08-14 a automação gera **dois calendários por semana, um por
canal**, não mais um único calendário de 6 posts:

| Canal | Posts | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" |
| Instagram | 4 | Segunda a quinta (sem post na sexta nem no sábado) | Rodízio entre Carrossel, Post estático, Reel |

Desde 2026-08-26, Família deixou de ser área própria do Instagram e virou
subtema de Cível — o banco de temas de Cível vive em `temas/civel/`, um
arquivo por subtema (ver passo 6 e `docs/formatos.md`, seção "Cível —
subtemas"). O total semanal passou de 9 para 8 posts.

Desde 2026-08-28, Previdenciário saiu do calendário editorial (decisão
editorial explícita do usuário, sem substituição por outra área ou dia) —
o Instagram deixou de publicar aos sábados e `temas/previdenciario.md` foi
removido. O total semanal passou de 8 para 7 posts.

Desde 2026-08-17, o LinkedIn é canal **100% B2B**, fixo em 3 áreas
(Empresarial, Trabalhista pelo ângulo empregador, Tributário — sem mais
rodízio de área), e alterna dois subtipos de registro (Autoridade técnica
80%, Informativo direto 20%) — ver `docs/formatos.md`.

Desde a mesma data, o banco "Posts" do Notion também é um **kanban de
produção** (Status com 6 etapas, Link da arte, Link do post, Responsável) e
acumula **métricas de desempenho** (Alcance, Curtidas, Comentários,
Compartilhamentos, Salvamentos, Cliques, Taxa de engajamento) preenchidas
manualmente pelo escritório — ver `docs/notion.md`.

## 0. Pré-condições

```
git pull origin main
```

Sempre antes de qualquer leitura ou escrita. Como a rotina escreve direto em
`main`, partir de um estado desatualizado é o único jeito de gerar conflito.

## 1. Verificar se há relatório de métricas pendente

No banco "Posts" do Notion, verifique os posts publicados há **~2 semanas**
(a semana `AAAA-SNN` cuja pasta em `calendarios/` ainda não tem
`relatorio.md`).

- **Se todos os posts dessa semana têm as métricas preenchidas** (7 posts
  desde que Previdenciário saiu do calendário em 2026-08-28, 8 posts nas
  semanas 2026-S35 e 2026-S36, 9 em semanas anteriores à reorganização de
  2026-08-26; Alcance e ao menos os campos de engajamento não vazios): há
  relatório pendente — gere-o no passo 2, antes de seguir para a semana
  nova.
- **Se as métricas ainda não foram preenchidas** (o escritório não teve
  tempo de olhar o Instagram Insights), **a semana já tem
  `relatorio.md`**, ou **não há semana ~2 anteriores ainda** (primeiras
  execuções do esquema de métricas): pule o passo 2 e vá direto ao passo 3.

Este passo nunca atrasa nem impede os passos 3–13 — é best-effort.

## 2. Gerar o relatório de métricas (só se o passo 1 identificou pendência)

A partir de `templates/relatorio-semanal.md`, para a semana identificada no
passo 1:

1. Puxe do Notion as propriedades de métrica dos posts daquela semana (7
   desde que Previdenciário saiu do calendário em 2026-08-28, 8 nas
   semanas 2026-S35 e 2026-S36, 9 em semanas anteriores à reorganização de
   temas de 2026-08-26).
2. Preencha cobertura de dados, ranking por taxa de engajamento, desempenho
   por área, desempenho por formato, erros e acertos.
3. Escreva no máximo 3 recomendações — cada uma **acionável** (muda uma
   escolha concreta de formato/área/tema/cadência) e **sóbria** (não
   superinterpreta amostra pequena). Nenhuma pode sugerir afrouxar
   `docs/normas-oab.md` — ver a trava em `docs/aprendizados.md`.
4. Salve como `calendarios/AAAA-SNN/relatorio.md` (a pasta da semana
   analisada, ~2 semanas atrás — não a semana nova que será gerada a
   partir do passo 3).
5. Publique como sub-página do Notion, irmã da sub-página "Semana NN" já
   existente daquela semana (ver `docs/notion.md`).
6. Faça append de cada recomendação como entrada nova em
   `docs/aprendizados.md`, no formato descrito no próprio arquivo.

## 3. Calcular a semana ISO alvo (semana nova)

- "Próxima semana" = próxima semana ISO completa (segunda a sábado) a
  partir da data de hoje. Se hoje é quinta (dia normal de execução da
  Routine), a próxima semana começa na segunda seguinte (4 dias depois).
- Nomeie a pasta de saída `calendarios/AAAA-SNN` usando o número da semana
  ISO (ex.: `2026-S34`).
- Determine a posição do ciclo do Instagram, que controla o formato (ver
  `docs/formatos.md` para as tabelas completas): `((N - 34) mod 3) + 1` —
  `N` é o número da semana ISO alvo; `34` é a âncora (semana 2026-S34,
  primeira execução do esquema de dois calendários, 2026-08-14).
- O LinkedIn não tem mais ciclo de semana — as 3 áreas são fixas todo
  período (ver passo 5). O que varia por post é o **subtipo de registro**
  (Autoridade técnica × Informativo direto), calculado no passo 5 a partir
  da contagem de posts de LinkedIn já publicados, não da semana ISO.

## 4. Ler o contexto antes de escrever qualquer coisa

Nesta ordem:
1. `docs/perfil-escritorio.md` — tom de voz, público, áreas, canais.
2. `docs/formatos.md` — canais, cadência, specs de formato, a matriz de
   rodízio área×dia×formato do Instagram que se aplica a esta semana, a
   área×dia fixa do LinkedIn e os dois subtipos de registro do LinkedIn.
3. `docs/normas-oab.md` — as 15 perguntas e o checklist bloqueante.
4. `temas/historico.md` — tudo que já foi publicado, nos dois canais, para
   não repetir.
5. `docs/aprendizados.md` — recomendações acumuladas de relatórios
   anteriores. Usa-se ao decidir formato/área/tema no passo 6, nunca para
   afrouxar o passo 9 (conformidade).

## 5. Definir os 7 posts da semana

**LinkedIn (3 posts)**: sempre as mesmas 3 áreas fixas — Empresarial
(segunda), Trabalhista (quarta, ângulo empregador/RH), Tributário (sexta)
— ver `docs/formatos.md`. Formato: sempre "Texto longo".

Para cada um dos 3, determine o **subtipo de registro**: conte quantas
linhas com `Canal = LinkedIn` existem em `temas/historico.md` antes desta
execução — esse número é o contador. Para cada novo post de LinkedIn desta
semana, incremente o contador em 1 e calcule `contador mod 5`: resultado
`4` → **Informativo direto**; resultados `0`–`3` → **Autoridade técnica**
(ver "Registro: dois subtipos" em `docs/formatos.md`). Isso mantém a
proporção 80/20 ao longo do tempo, incremental a cada post, não só dentro
da semana.

**Instagram (4 posts)**: uma área por dia, segunda a quinta (sem post na
sexta nem no sábado), fixo (ver `docs/formatos.md`). Formato de cada dia
vem da semana do ciclo do Instagram calculada no passo 3.

Isso dá uma lista de 7 (área, canal, dia, formato, e para LinkedIn também o
subtipo de registro) para os quais escolher tema.

## 6. Selecionar o tema de cada um dos 7 posts

Para cada item da lista do passo 5:

- Abra `temas/<area>.md` e pegue o primeiro tema da fila que **não**
  apareça em `temas/historico.md` — a checagem é global entre os dois
  canais: um tema usado no Instagram não pode reaparecer no LinkedIn (nem
  vice-versa), mesmo que a área seja a mesma.
- **Exceção — Cível (terça-feira)**: não há `temas/civel.md`. Abra os 5
  arquivos de `temas/civel/` (`imobiliario.md`, `familia.md`,
  `responsabilidade-civil.md`, `direito-das-coisas.md`, `contratos.md`,
  nessa ordem) e pegue o primeiro tema elegível entre todos eles, mesma
  regra de anti-repetição — sem preferência fixa por subtema. Registre o
  subtema escolhido no campo Tema do briefing (ex.: "Família — União
  estável..."); no Notion, `Área` continua "Cível" (ver `docs/notion.md`).
- Empresarial, Trabalhista e Tributário aparecem nos dois canais **toda
  semana** (são as 3 áreas fixas do LinkedIn, e também têm dia fixo no
  Instagram) — use sempre dois temas diferentes do banco daquela área, um
  para cada canal, nunca o mesmo tema nos dois na mesma semana.
- Considere `docs/aprendizados.md`: se houver uma recomendação ativa sobre
  área/tema (ex.: "priorizar temas de X"), aplique-a como critério de
  desempate entre temas igualmente elegíveis — nunca como critério que pule
  a fila de anti-repetição.
- **Se houver acesso à web nesta execução**: antes de usar o banco, avalie
  se há uma mudança legislativa ou decisão relevante do STF/STJ/TST recente
  e mais pertinente que o próximo item do banco. Se houver, use-a no lugar
  — registre a fonte (norma/decisão) no briefing, seção 1.
- **Se não houver acesso à web**: use o banco e siga em frente. Isso nunca
  bloqueia a execução.
- Temas de risco "Alto" (marcados no banco) exigem atenção redobrada nos
  passos 8 e 9, não exclusão automática.

## 7. Formato de cada post

Já determinado no passo 5 — LinkedIn é sempre "Texto longo"; o formato de
cada post do Instagram vem da matriz de rodízio da semana do ciclo
calculada no passo 3. `docs/aprendizados.md` pode influenciar qual **área**
ganha qual **tema** (passo 6), nunca a matriz de rodízio de formato em si —
mudar o rodízio é decisão editorial explícita do usuário, feita fora do
fluxo automático (ver `CLAUDE.md`).

## 8. Redigir os 7 briefings

Um arquivo por post, a partir de `templates/briefing-post.md`, com todas as
8 seções preenchidas (incluindo o campo **Canal** no cabeçalho) e a copy
final pronta para arte — sem placeholder, sem colchete sobrando. Escreva no
tom de `docs/perfil-escritorio.md`.

Para os 3 posts do LinkedIn especificamente: escreva sempre para público
exclusivamente PJ (gestores, sócios, jurídico interno, RH, financeiro —
nunca "você" genérico de pessoa física), no subtipo determinado no passo 5
(Autoridade técnica ou Informativo direto — specs completas em
`docs/formatos.md`). Trabalhista no LinkedIn é sempre pelo ângulo
empregador/RH, mesmo que `temas/trabalhista.md` liste público misto para
aquele tema. Registrar o subtipo escolhido no cabeçalho do briefing (seção
1, campo novo "Subtipo LinkedIn").

## 9. Rodar o checklist OAB peça por peça

Para cada um dos 7 briefings, aplique as 8 regras de
`docs/normas-oab.md` (seção "Checklist operacional") item a item. Se
qualquer item ficar "Revisar": reescreva a copy até resolver — nunca publique
com item pendente. Preencha a seção 7 do briefing com o resultado.

Rode também a varredura de termos-gatilho (lista no fim de
`docs/normas-oab.md`) sobre a copy final de cada peça, como segunda
checagem.

Este passo é **inegociável e não é influenciado por `docs/aprendizados.md`**
— nenhuma recomendação de desempenho pode reduzir o rigor aqui.

## 10. Salvar em `calendarios/AAAA-SNN/` (semana nova)

- `calendario.md` — a partir de `templates/calendario-semanal.md`,
  panorama da semana com os dois calendários (LinkedIn e Instagram) e link
  para cada arquivo de post.
- `linkedin/NN-dia-area.md` — os 3 posts do LinkedIn (`01-segunda-area.md`,
  `02-quarta-area.md`, `03-sexta-area.md`).
- `instagram/NN-dia-area.md` — os 4 posts do Instagram
  (`01-segunda-empresarial.md` até `04-quinta-tributario.md`).

## 11. Atualizar `temas/historico.md`

Append de uma linha por post publicado (data, semana, área, canal,
formato, tema, link do Notion), um por um dos 7 posts. Nunca reescrever
linhas existentes.

## 12. Publicar no Notion

Siga `docs/notion.md`:
1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever.
2. Criar as 7 páginas no data source "Posts" (`Status = "Em aprovação"`,
   `Canal` preenchido com "LinkedIn" ou "Instagram", campos de kanban —
   Link da arte, Link do post, Responsável — e de métrica em branco), com o
   briefing completo como conteúdo da página.
3. Criar a sub-página da semana em Calendário Editorial, com o panorama dos
   dois calendários e `<mention-page>` para os 7 posts.
4. Atualizar a tabela de sub-páginas em `docs/notion.md`.

Se o conector do Notion não estiver disponível nesta execução: pule este
passo (e o passo 2, se aplicável), mas conclua os demais passos
normalmente, e registre a omissão explicitamente (ver passo 14).

## 13. Commitar e dar push em `main`

```
git add calendarios/ temas/historico.md docs/notion.md docs/aprendizados.md
git commit -m "Calendário editorial — Semana NN/AAAA"
git push origin main
```

O commit semanal só deve tocar esses arquivos — nunca reescrever
documentação estrutural, templates ou o corpo do banco de temas na mesma
execução. (`docs/notion.md` e `docs/aprendizados.md` são exceções: só a
tabela de sub-páginas semanais e o append de novas entradas, respectivamente
— o resto de cada arquivo não muda.)

## 14. Se algum passo falhar

Conclua todos os outros passos possíveis. Declare explicitamente o que
ficou de fora e por quê — e em qual canal, se for o caso:
- Na mensagem de commit (linha extra depois do título).
- Na seção "Pendências / o que ficou de fora" de `calendario.md`.
- Na sub-página do Notion, se ela foi criada (seção "Notas da semana").

Nunca deixe a execução silenciosamente incompleta.
