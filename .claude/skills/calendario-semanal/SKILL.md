---
name: calendario-semanal
description: Gera dois calendários editoriais semanais separados — LinkedIn (3 posts) e Instagram (6 posts, um por área do direito) — do escritório Gutmann & Silva, aplica o checklist de conformidade OAB, gera o relatório de métricas pendente, publica no Notion e comita em main. Use quando disparado pela Routine de quinta-feira ou quando pedirem para gerar/ensaiar o calendário de uma semana.
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

- **Se todos os 9 posts dessa semana têm as métricas preenchidas** (Alcance
  e ao menos os campos de engajamento não vazios): há relatório pendente —
  gere-o no passo 2, antes de seguir para a semana nova.
- **Se as métricas ainda não foram preenchidas** (o escritório não teve
  tempo de olhar o Instagram Insights), **a semana já tem
  `relatorio.md`**, ou **não há semana ~2 anteriores ainda** (primeiras
  execuções do esquema de métricas): pule o passo 2 e vá direto ao passo 3.

Este passo nunca atrasa nem impede os passos 3–13 — é best-effort.

## 2. Gerar o relatório de métricas (só se o passo 1 identificou pendência)

A partir de `templates/relatorio-semanal.md`, para a semana identificada no
passo 1:

1. Puxe do Notion as propriedades de métrica dos 9 posts daquela semana.
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
- Determine as duas posições de ciclo que se aplicam a esta semana (ver
  `docs/formatos.md` para as tabelas completas):
  - **Ciclo do Instagram** (3 semanas, controla o formato):
    `((N - 34) mod 3) + 1`.
  - **Ciclo do LinkedIn** (2 semanas, controla o grupo de 3 áreas):
    `(N - 34) mod 2` — `0` = Grupo 1, `1` = Grupo 2.
  - `N` é o número da semana ISO alvo; `34` é a âncora — a semana 2026-S34
    foi regenerada em 2026-08-14 como a primeira execução real deste
    esquema de dois calendários, substituindo o ensaio anterior (esquema
    antigo de 1 calendário só).

## 4. Ler o contexto antes de escrever qualquer coisa

Nesta ordem:
1. `docs/perfil-escritorio.md` — tom de voz, público, áreas, canais.
2. `docs/formatos.md` — canais, cadência, specs de formato e as duas
   matrizes de rodízio (área×dia×formato do Instagram; área×dia do
   LinkedIn) que se aplicam a esta semana.
3. `docs/normas-oab.md` — as 15 perguntas e o checklist bloqueante.
4. `temas/historico.md` — tudo que já foi publicado, nos dois canais, para
   não repetir.
5. `docs/aprendizados.md` — recomendações acumuladas de relatórios
   anteriores. Usa-se ao decidir formato/área/tema no passo 6, nunca para
   afrouxar o passo 9 (conformidade).

## 5. Definir os 9 posts da semana

**LinkedIn (3 posts)**: usando o grupo do ciclo do LinkedIn calculado no
passo 3, pegue as 3 áreas de `docs/formatos.md` (Grupo 1 ou Grupo 2) e seus
dias fixos (segunda/quarta/sexta). Formato: sempre "Texto longo".

**Instagram (6 posts)**: uma área por dia, segunda a sábado, fixo (ver
`docs/formatos.md`). Formato de cada dia vem da semana do ciclo do
Instagram calculada no passo 3.

Isso dá uma lista de 9 (área, canal, dia, formato) para os quais escolher
tema.

## 6. Selecionar o tema de cada um dos 9 posts

Para cada item da lista do passo 5:

- Abra `temas/<area>.md` e pegue o primeiro tema da fila que **não**
  apareça em `temas/historico.md` — a checagem é global entre os dois
  canais: um tema usado no Instagram não pode reaparecer no LinkedIn (nem
  vice-versa), mesmo que a área seja a mesma.
- Se a mesma área tiver posts nos dois canais na mesma semana (possível
  quando o grupo do LinkedIn coincide com aquele dia do Instagram), use
  dois temas diferentes do banco daquela área — nunca o mesmo tema nos dois
  canais na mesma semana.
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

## 8. Redigir os 9 briefings

Um arquivo por post, a partir de `templates/briefing-post.md`, com todas as
8 seções preenchidas (incluindo o campo **Canal** no cabeçalho) e a copy
final pronta para arte — sem placeholder, sem colchete sobrando. Escreva no
tom de `docs/perfil-escritorio.md`.

## 9. Rodar o checklist OAB peça por peça

Para cada um dos 9 briefings, aplique as 8 regras de
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
- `instagram/NN-dia-area.md` — os 6 posts do Instagram
  (`01-segunda-empresarial.md` até `06-sabado-previdenciario.md`).

## 11. Atualizar `temas/historico.md`

Append de uma linha por post publicado (data, semana, área, canal,
formato, tema, link do Notion), um por um dos 9 posts. Nunca reescrever
linhas existentes.

## 12. Publicar no Notion

Siga `docs/notion.md`:
1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever.
2. Criar as 9 páginas no data source "Posts" (`Status = "Em aprovação"`,
   `Canal` preenchido com "LinkedIn" ou "Instagram", campos de kanban —
   Link da arte, Link do post, Responsável — e de métrica em branco), com o
   briefing completo como conteúdo da página.
3. Criar a sub-página da semana em Calendário Editorial, com o panorama dos
   dois calendários e `<mention-page>` para os 9 posts.
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
