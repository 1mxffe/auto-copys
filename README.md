# auto-copys

Automação do calendário editorial semanal do escritório **Gutmann & Silva**.
Toda sexta às 8h, uma Routine do Claude Code gera 6 briefings de post — um
por área do direito —, confere cada um contra o checklist de conformidade da
OAB, publica no Notion e comita direto na branch `main` deste repositório.

## Como funciona

```
sexta 8h ──► Routine dispara sessão nova
             │
             ├─ 1. git pull origin main
             ├─ 2. lê perfil, formatos, normas OAB, histórico de temas
             ├─ 3. escolhe 6 temas (banco de temas, ou atualidade se houver web)
             ├─ 4. define rodízio de formato por área (ciclo de 3 semanas)
             ├─ 5. escreve 6 briefings completos (copy final incluída)
             ├─ 6. roda o checklist OAB peça por peça — reescreve se necessário
             ├─ 7. salva em calendarios/AAAA-SNN/, atualiza temas/historico.md
             ├─ 8. publica no Notion (database "Posts" + sub-página da semana)
             └─ 9. commit + push direto em main (sem PR)
```

O procedimento completo está em
[`.claude/skills/calendario-semanal/SKILL.md`](.claude/skills/calendario-semanal/SKILL.md).
O prompt colado na Routine está em [`PROMPT_ROTINA.md`](PROMPT_ROTINA.md) —
propositalmente curto, porque a lógica toda vive na skill.

## Fonte da verdade

O Markdown neste repositório é a fonte da verdade — versionado, revisável em
diff. O Notion é a camada de **publicação e aprovação**: cada post vira uma
linha no banco "Posts" sob a página **Calendário Editorial**, com o
briefing completo no corpo da página, e a aprovação editorial acontece lá,
pelo campo **Status** (Rascunho → Em aprovação → Aprovado → Publicado) — não
neste repositório, e não por Pull Request.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `CLAUDE.md` | Contexto carregado em toda sessão deste repositório |
| `.claude/skills/calendario-semanal/` | Procedimento completo, passo a passo |
| `docs/normas-oab.md` | As 15 perguntas da Cartilha CFOAB + checklist bloqueante |
| `docs/perfil-escritorio.md` | Marca, tom de voz, público, áreas |
| `docs/formatos.md` | Specs dos 5 formatos + matriz de rodízio |
| `docs/notion.md` | IDs do Notion e como publicar |
| `templates/` | Template de briefing e de panorama semanal |
| `temas/<area>.md` | Banco de temas evergreen, 6 arquivos |
| `temas/historico.md` | Anti-repetição — tudo já publicado |
| `calendarios/AAAA-SNN/` | Saída de cada semana |

## Conformidade OAB

Cada briefing carrega, na sua seção 7, a prova de que passou pelo checklist
derivado da Cartilha do CFOAB "Principais dúvidas sobre Publicidade na
Advocacia: entendendo o Provimento 205/2021" — sem promessa de resultado,
sem caso concreto de cliente, sem CTA de conversão, sem linguagem de
urgência. Ver `docs/normas-oab.md` para o detalhe de cada regra e exemplos
de reescrita.

## Fora de escopo

- Geração de arte/design visual — o entregável é briefing + copy.
- Publicação automática em redes sociais — a rotina para na aprovação
  (Status no Notion).
- Métricas de desempenho dos posts.

## Operação

- **Rodar manualmente**: peça para o Claude Code, neste repositório, seguir
  a skill `calendario-semanal`.
- **Renovar a Routine**: Routines recorrentes podem expirar após um período
  em algumas configurações de agendamento. Verifique periodicamente se a
  Routine segue ativa (`next_run_at` no futuro) e recrie com os parâmetros
  de `PROMPT_ROTINA.md` se necessário.
