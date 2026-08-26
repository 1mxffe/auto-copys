# CLAUDE.md — Automação de calendário editorial · Gutmann & Silva

Este repositório é a fonte da verdade para o calendário editorial semanal do
escritório Gutmann & Silva. Toda sessão do Claude Code aberta aqui — manual ou
disparada pela Routine semanal — deve carregar este contexto antes de agir.

## O que este repositório é

Uma automação que gera, semana a semana, **dois calendários editoriais
separados** — um por canal, cada um com a própria cadência — passa cada
peça pelo checklist de conformidade da OAB (Provimento 205/2021), grava
tudo em Markdown versionado e publica a mesma informação em um banco de
dados no Notion, sob a página **Calendário Editorial**.

O Markdown em `calendarios/` é a fonte da verdade. O Notion é a camada de
publicação e aprovação — a camada onde o time efetivamente aprova ou pede
ajuste, pelo campo **Status**.

## Regras que não mudam

- **Volume**: 8 posts por semana, em dois calendários de canal
  independentes — **LinkedIn**: 3 posts (segunda, quarta, sexta), sempre
  formato "Texto longo". **Instagram**: 5 posts (segunda a quinta e
  sábado — sem post na sexta), um por área — Empresarial, Cível,
  Trabalhista, Tributário, Previdenciário —, formato em rodízio. Regras
  completas de área × dia × formato por canal em `docs/formatos.md`.
- **Cível tem subtemas, é a única área que os tem**: desde 2026-08-26,
  Cível é dividida em 5 subtemas — Imobiliário, Família, Responsabilidade
  Civil, Direito das coisas, Contratos —, cada um com o próprio banco em
  `temas/civel/<subtema>.md`. Família deixou de ser área própria do
  calendário (não tem mais dia fixo isolado no Instagram) e virou um
  desses 5 subtemas; a terça-feira de Cível escolhe, semana a semana,
  entre os 5 arquivos pela mesma regra de anti-repetição, sem preferência
  fixa por subtema — ver `docs/formatos.md`.
- **Trabalhista tem dois ângulos, um arquivo só**: `temas/trabalhista.md`
  continua um banco único (sem subpastas), mas cada tema indica se o
  ângulo predominante é do reclamante, do reclamado, ou de ambos —
  informação para quem escreve o briefing, não um novo nível de pasta. No
  LinkedIn o enquadramento continua sempre pelo lado do reclamado
  (empregador/RH), independente dessa marcação.
- **LinkedIn é canal 100% B2B**: existe para atrair empresas e reforçar o
  escritório como referência técnica. Só 3 áreas, fixas, sem rodízio —
  Empresarial, Trabalhista (sempre ângulo empregador/RH), Tributário.
  Cível (incluindo o subtema Família) e Previdenciário ficam só no
  Instagram. 80% dos posts do LinkedIn em registro "Autoridade técnica",
  20% "Informativo direto" — ver `docs/formatos.md`. Autoridade se
  constrói pela precisão da análise, nunca por autoelogio — isso não abre
  exceção nenhuma no checklist de `docs/normas-oab.md`.
- **Git**: commit direto na branch `main`, sem Pull Request. `git pull origin
  main` sempre antes de commitar. O commit semanal só deve tocar
  `calendarios/<semana nova>/` e o append em `temas/historico.md` — nunca
  reescrever documentação, templates ou banco de temas dentro da mesma
  execução automatizada.
- **Conformidade OAB é bloqueante**: nenhuma peça é gravada em
  `calendarios/` ou publicada no Notion sem passar pelo checklist de
  `docs/normas-oab.md`, item por item, registrado no próprio briefing.
- **Anti-repetição**: nenhum tema sai duas vezes. Consulte
  `temas/historico.md` antes de escolher pauta; grave a entrada nova ao final
  da execução.
- **Rede é opcional, nunca bloqueante**: se houver acesso à web, prefira
  pauta de atualidade jurídica relevante (mudança legislativa, decisão do
  STF/STJ/TST) no lugar de um tema do banco. Se não houver rede, use o banco
  de temas e siga em frente — a rotina nunca falha por falta de acesso à
  internet.
- **Conformidade nunca cede a métrica**: o relatório semanal de resultados
  (`docs/aprendizados.md`, `templates/relatorio-semanal.md`) pode recomendar
  ajuste de formato, área, tema ou cadência — nunca pode sugerir afrouxar um
  item de `docs/normas-oab.md`. Otimizar por engajamento é exatamente a
  pressão que empurra copy para urgência e sensacionalismo; essa pressão
  perde sempre.
- **Fora de escopo**: geração de arte/design visual, publicação automática
  em redes sociais, automação da coleta de métricas via API (a entrada é
  manual — ver `docs/notion.md`). O entregável é briefing + copy; a
  aprovação humana no Notion é o portão antes de qualquer publicação real.

## Onde está cada coisa

| Caminho | Conteúdo |
|---|---|
| `.claude/skills/calendario-semanal/SKILL.md` | Procedimento completo, passo a passo, usado pela Routine e por execuções manuais |
| `docs/normas-oab.md` | Transcrição das 15 perguntas da Cartilha CFOAB + checklist operacional bloqueante |
| `docs/perfil-escritorio.md` | Marca, tom de voz, público-alvo, áreas de atuação |
| `docs/formatos.md` | Canais, cadência, specs de formato e as matrizes de rodízio de cada canal (área × dia × formato) |
| `docs/notion.md` | IDs do Notion (página, database, views) e como publicar |
| `templates/briefing-post.md` | Template de briefing por post — 8 seções, espelha o `.docx` original |
| `templates/calendario-semanal.md` | Template do panorama semanal (dois calendários, um por canal) |
| `templates/relatorio-semanal.md` | Template do relatório de métricas — ranking, desempenho por área/formato, recomendações |
| `docs/aprendizados.md` | Registro cumulativo de recomendações de desempenho, consultado ao escolher tema/área |
| `temas/<area>.md` (Empresarial, Trabalhista, Tributário, Previdenciário) e `temas/civel/<subtema>.md` (Imobiliário, Família, Responsabilidade Civil, Direito das coisas, Contratos) | Banco de temas evergreen — um arquivo por área, exceto Cível, dividida em 5 subtemas |
| `temas/historico.md` | Registro de tudo já publicado — consultado para evitar repetição |
| `calendarios/AAAA-SNN/` | Saída de cada semana: `calendario.md` (panorama dos dois canais) + `linkedin/` e `instagram/` (um arquivo por post) + `relatorio.md` (quando gerado, ~2 semanas depois) |

## Antes de qualquer execução

1. Leia `docs/perfil-escritorio.md`, `docs/formatos.md`, `docs/normas-oab.md`
   e `temas/historico.md`.
2. Se for publicar no Notion, leia `notion://docs/enhanced-markdown-spec` via
   `notion-fetch` antes de escrever — não adivinhe a sintaxe de Notion
   Markdown.
3. Use os IDs já gravados em `docs/notion.md`; não recrie a estrutura do
   banco "Posts" a cada execução.

## Convenção de nomes

- Semana ISO: pasta `calendarios/AAAA-SNN` (ex.: `calendarios/2026-S34`).
- Post do LinkedIn: `calendarios/AAAA-SNN/linkedin/NN-dia-area.md` (ex.:
  `01-segunda-empresarial.md`).
- Post do Instagram: `calendarios/AAAA-SNN/instagram/NN-dia-area.md` (ex.:
  `01-segunda-empresarial.md`).
- Commit semanal: `Calendário editorial — Semana NN/AAAA`.
