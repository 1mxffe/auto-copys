---
name: calendario-semanal
description: Gera dois calendários editoriais semanais separados — LinkedIn (3 posts) e Instagram (6 posts, um por área do direito) — do escritório Gutmann & Silva, aplica o checklist de conformidade OAB, publica no Notion e comita em main. Use quando disparado pela Routine de sexta-feira ou quando pedirem para gerar/ensaiar o calendário de uma semana.
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
| Instagram | 6 | Segunda a sábado | Rodízio entre Carrossel, Post estático, Reel |

## 0. Pré-condições

```
git pull origin main
```

Sempre antes de qualquer leitura ou escrita. Como a rotina escreve direto em
`main`, partir de um estado desatualizado é o único jeito de gerar conflito.

## 1. Calcular a semana ISO alvo

- "Próxima semana" = próxima semana ISO completa (segunda a sábado) a
  partir da data de hoje. Se hoje é sexta, a próxima semana começa na
  segunda seguinte (3 dias depois).
- Nomeie a pasta de saída `calendarios/AAAA-SNN` usando o número da semana
  ISO (ex.: `2026-S35`).
- Determine as duas posições de ciclo que se aplicam a esta semana (ver
  `docs/formatos.md` para as tabelas completas):
  - **Ciclo do Instagram** (3 semanas, controla o formato):
    `((N - 35) mod 3) + 1`.
  - **Ciclo do LinkedIn** (2 semanas, controla o grupo de 3 áreas):
    `(N - 35) mod 2` — `0` = Grupo 1, `1` = Grupo 2.
  - `N` é o número da semana ISO alvo; `35` é a âncora porque a semana 34
    foi o ensaio manual, sob o esquema antigo de 1 calendário só. Se esta
    execução for um ensaio/primeira execução real do novo esquema, trate a
    semana atual como se fosse a semana 35 (ciclo do Instagram = semana 1,
    ciclo do LinkedIn = Grupo 1).

## 2. Ler o contexto antes de escrever qualquer coisa

Nesta ordem:
1. `docs/perfil-escritorio.md` — tom de voz, público, áreas, canais.
2. `docs/formatos.md` — canais, cadência, specs de formato e as duas
   matrizes de rodízio (área×dia×formato do Instagram; área×dia do
   LinkedIn) que se aplicam a esta semana.
3. `docs/normas-oab.md` — as 15 perguntas e o checklist bloqueante.
4. `temas/historico.md` — tudo que já foi publicado, nos dois canais, para
   não repetir.

## 3. Definir os 9 posts da semana

**LinkedIn (3 posts)**: usando o grupo do ciclo do LinkedIn calculado no
passo 1, pegue as 3 áreas de `docs/formatos.md` (Grupo 1 ou Grupo 2) e seus
dias fixos (segunda/quarta/sexta). Formato: sempre "Texto longo".

**Instagram (6 posts)**: uma área por dia, segunda a sábado, fixo (ver
`docs/formatos.md`). Formato de cada dia vem da semana do ciclo do
Instagram calculada no passo 1.

Isso dá uma lista de 9 (área, canal, dia, formato) para os quais escolher
tema.

## 4. Selecionar o tema de cada um dos 9 posts

Para cada item da lista do passo 3:

- Abra `temas/<area>.md` e pegue o primeiro tema da fila que **não**
  apareça em `temas/historico.md` — a checagem é global entre os dois
  canais: um tema usado no Instagram não pode reaparecer no LinkedIn (nem
  vice-versa), mesmo que a área seja a mesma.
- Se a mesma área tiver posts nos dois canais na mesma semana (possível
  quando o grupo do LinkedIn coincide com aquele dia do Instagram), use
  dois temas diferentes do banco daquela área — nunca o mesmo tema nos dois
  canais na mesma semana.
- **Se houver acesso à web nesta execução**: antes de usar o banco, avalie
  se há uma mudança legislativa ou decisão relevante do STF/STJ/TST recente
  e mais pertinente que o próximo item do banco. Se houver, use-a no lugar
  — registre a fonte (norma/decisão) no briefing, seção 1.
- **Se não houver acesso à web**: use o banco e siga em frente. Isso nunca
  bloqueia a execução.
- Temas de risco "Alto" (marcados no banco) exigem atenção redobrada nos
  passos 6 e 7, não exclusão automática.

## 5. Formato de cada post

Já determinado no passo 3 — LinkedIn é sempre "Texto longo"; o formato de
cada post do Instagram vem da matriz de rodízio da semana do ciclo
calculada no passo 1 (`docs/formatos.md`).

## 6. Redigir os 9 briefings

Um arquivo por post, a partir de `templates/briefing-post.md`, com todas as
8 seções preenchidas (incluindo o campo **Canal** no cabeçalho) e a copy
final pronta para arte — sem placeholder, sem colchete sobrando. Escreva no
tom de `docs/perfil-escritorio.md`.

## 7. Rodar o checklist OAB peça por peça

Para cada um dos 9 briefings, aplique as 8 regras de
`docs/normas-oab.md` (seção "Checklist operacional") item a item. Se
qualquer item ficar "Revisar": reescreva a copy até resolver — nunca publique
com item pendente. Preencha a seção 7 do briefing com o resultado.

Rode também a varredura de termos-gatilho (lista no fim de
`docs/normas-oab.md`) sobre a copy final de cada peça, como segunda
checagem.

## 8. Salvar em `calendarios/AAAA-SNN/`

- `calendario.md` — a partir de `templates/calendario-semanal.md`,
  panorama da semana com os dois calendários (LinkedIn e Instagram) e link
  para cada arquivo de post.
- `linkedin/NN-dia-area.md` — os 3 posts do LinkedIn (`01-segunda-area.md`,
  `02-quarta-area.md`, `03-sexta-area.md`).
- `instagram/NN-dia-area.md` — os 6 posts do Instagram
  (`01-segunda-empresarial.md` até `06-sabado-previdenciario.md`).

## 9. Atualizar `temas/historico.md`

Append de uma linha por post publicado (data, semana, área, **canal**,
formato, tema, link do Notion), um por um dos 9 posts. Nunca reescrever
linhas existentes.

## 10. Publicar no Notion

Siga `docs/notion.md`:
1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever.
2. Criar as 9 páginas no data source "Posts" (`Status = "Em aprovação"`,
   `Canal` preenchido com "LinkedIn" ou "Instagram"), com o briefing
   completo como conteúdo da página.
3. Criar a sub-página da semana em Calendário Editorial, com o panorama dos
   dois calendários e `<mention-page>` para os 9 posts.
4. Atualizar a tabela de sub-páginas em `docs/notion.md`.

Se o conector do Notion não estiver disponível nesta execução: pule este
passo, mas conclua os passos 1–9 e 11 normalmente, e registre a omissão
explicitamente (ver passo 12).

## 11. Commitar e dar push em `main`

```
git add calendarios/AAAA-SNN/ temas/historico.md docs/notion.md
git commit -m "Calendário editorial — Semana NN/AAAA"
git push origin main
```

O commit semanal só deve tocar esses arquivos — nunca reescrever
documentação, templates ou o corpo do banco de temas na mesma execução.
(`docs/notion.md` é a exceção: só a tabela de sub-páginas semanais é
apendada, o resto do arquivo não muda.)

## 12. Se algum passo falhar

Conclua todos os outros passos possíveis. Declare explicitamente o que
ficou de fora e por quê — e em qual canal, se for o caso:
- Na mensagem de commit (linha extra depois do título).
- Na seção "Pendências / o que ficou de fora" de `calendario.md`.
- Na sub-página do Notion, se ela foi criada (seção "Notas da semana").

Nunca deixe a execução silenciosamente incompleta.
