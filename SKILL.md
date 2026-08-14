---
name: calendario-semanal
description: Gera o calendário editorial semanal (6 posts, um por área do direito) do escritório Gutmann & Silva, aplica o checklist de conformidade OAB, publica no Notion e comita em main. Use quando disparado pela Routine de sexta-feira ou quando pedirem para gerar/ensaiar o calendário de uma semana.
---

# Calendário editorial semanal — Gutmann & Silva

Procedimento completo. O prompt da Routine (`PROMPT_ROTINA.md`) é
deliberadamente curto porque toda a lógica vive aqui — mudanças de processo
devem ser feitas neste arquivo, não no prompt.

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
  ISO (ex.: `2026-S34`).
- Determine a posição no ciclo de rodízio de formatos:
  `((N - 34) mod 3) + 1`, onde `N` é o número da semana ISO e `34` é a
  semana da primeira execução (ver `docs/formatos.md`). Se este for um
  ensaio/primeira execução real, semana 34 = semana 1 do ciclo.

## 2. Ler o contexto antes de escrever qualquer coisa

Nesta ordem:
1. `docs/perfil-escritorio.md` — tom de voz, público, áreas.
2. `docs/formatos.md` — specs de formato e a linha do ciclo de rodízio que
   se aplica a esta semana.
3. `docs/normas-oab.md` — as 15 perguntas e o checklist bloqueante.
4. `temas/historico.md` — tudo que já foi publicado, para não repetir.

## 3. Selecionar 6 temas (um por área)

Para cada área (Empresarial, Cível, Trabalhista, Tributário, Família,
Previdenciário):

- Abra `temas/<area>.md` e pegue o primeiro tema da fila que **não** apareça
  em `temas/historico.md`.
- **Se houver acesso à web nesta execução**: antes de usar o banco, avalie
  se há uma mudança legislativa ou decisão relevante do STF/STJ/TST recente
  e mais pertinente que o próximo item do banco. Se houver, use-a no lugar
  — registre a fonte (norma/decisão) no briefing, seção 1.
- **Se não houver acesso à web**: use o banco e siga em frente. Isso nunca
  bloqueia a execução.
- Temas de risco "Alto" (marcados no banco) exigem atenção redobrada nos
  passos 5 e 6, não exclusão automática.

## 4. Definir o rodízio de formatos da semana

Use a linha do ciclo calculada no passo 1 (`docs/formatos.md`). Cada área
recebe o formato indicado para aquela semana do ciclo de 3 semanas.

## 5. Redigir os 6 briefings

Um arquivo por post, a partir de `templates/briefing-post.md`, com todas as
8 seções preenchidas e a copy final pronta para arte — sem placeholder, sem
colchete sobrando. Escreva no tom de `docs/perfil-escritorio.md`.

## 6. Rodar o checklist OAB peça por peça

Para cada um dos 6 briefings, aplique as 8 regras de
`docs/normas-oab.md` (seção "Checklist operacional") item a item. Se
qualquer item ficar "Revisar": reescreva a copy até resolver — nunca publique
com item pendente. Preencha a seção 7 do briefing com o resultado.

Rode também a varredura de termos-gatilho (lista no fim de
`docs/normas-oab.md`) sobre a copy final de cada peça, como segunda
checagem.

## 7. Salvar em `calendarios/AAAA-SNN/`

- `calendario.md` — a partir de `templates/calendario-semanal.md`,
  panorama da semana com link para cada arquivo de post.
- `NN-dia-area.md` — um arquivo por post (`01-segunda-empresarial.md` até
  `06-sabado-previdenciario.md`).

## 8. Atualizar `temas/historico.md`

Append de uma linha por post publicado (data, semana, área, formato, tema,
link do Notion). Nunca reescrever linhas existentes.

## 9. Publicar no Notion

Siga `docs/notion.md`:
1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever.
2. Criar as 6 páginas no data source "Posts" (`Status = "Em aprovação"`),
   com o briefing completo como conteúdo da página.
3. Criar a sub-página da semana em Calendário Editorial, com o panorama e
   `<mention-page>` para os 6 posts.
4. Atualizar a tabela de sub-páginas em `docs/notion.md`.

Se o conector do Notion não estiver disponível nesta execução: pule este
passo, mas conclua os passos 1–8 e 10 normalmente, e registre a omissão
explicitamente (ver passo 11).

## 10. Commitar e dar push em `main`

```
git add calendarios/AAAA-SNN/ temas/historico.md docs/notion.md
git commit -m "Calendário editorial — Semana NN/AAAA"
git push origin main
```

O commit semanal só deve tocar esses arquivos — nunca reescrever
documentação, templates ou o corpo do banco de temas na mesma execução.
(`docs/notion.md` é a exceção: só a tabela de sub-páginas semanais é
apendada, o resto do arquivo não muda.)

## 11. Se algum passo falhar

Conclua todos os outros passos possíveis. Declare explicitamente o que
ficou de fora e por quê:
- Na mensagem de commit (linha extra depois do título).
- Na seção "Pendências / o que ficou de fora" de `calendario.md`.
- Na sub-página do Notion, se ela foi criada (seção "Notas da semana").

Nunca deixe a execução silenciosamente incompleta.
