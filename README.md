# auto-copys

Automação do calendário editorial semanal do escritório **Gutmann & Silva**.
Toda quinta às 8h (Brasília), uma Routine do Claude Code gera **dois
calendários separados** — LinkedIn (3 posts/semana, 100% B2B, para atrair
empresas) e Instagram (6 posts/semana, um por área) —, confere cada peça
contra o checklist de conformidade da OAB, publica no Notion e comita
direto na branch `main` deste repositório.

## Como funciona

```
quinta 8h (Brasília) ──► Routine dispara sessão nova
             │
             ├─ 1. git pull origin main
             ├─ 2. verifica se há relatório de métricas pendente (posts de
             │      ~2 semanas atrás já com número no Notion); se houver,
             │      gera o relatório e atualiza docs/aprendizados.md ANTES
             │      de seguir
             ├─ 3. lê perfil, formatos/canais, normas OAB, histórico de
             │      temas e aprendizados de desempenho
             ├─ 4. escolhe os temas dos 9 posts (banco de temas, ou
             │      atualidade se houver web) — 3 para LinkedIn, 6 para
             │      Instagram, sem repetir nada do histórico entre os canais
             ├─ 5. define área×dia×formato do Instagram (rodízio) e o
             │      subtipo de registro de cada post do LinkedIn (Autoridade
             │      técnica 80% / Informativo direto 20% — área é sempre
             │      Empresarial/Trabalhista/Tributário, sem rodízio)
             ├─ 6. escreve os 9 briefings completos (copy final incluída)
             ├─ 7. roda o checklist OAB peça por peça — reescreve se
             │      necessário (este passo nunca é afrouxado por métrica)
             ├─ 8. salva em calendarios/AAAA-SNN/{linkedin,instagram}/,
             │      atualiza temas/historico.md
             ├─ 9. publica no Notion (database "Posts", campo Canal
             │      preenchido, + sub-página da semana com os dois
             │      calendários; campos de kanban e métrica em branco)
             └─ 10. commit + push direto em main (sem PR)
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
| `docs/formatos.md` | Canais (LinkedIn/Instagram), cadência, specs de formato e matrizes de rodízio de cada canal |
| `docs/notion.md` | IDs do Notion e como publicar |
| `templates/` | Template de briefing, de panorama semanal e de relatório de métricas |
| `docs/aprendizados.md` | Recomendações de desempenho acumuladas, semana a semana |
| `temas/<area>.md` | Banco de temas evergreen, 6 arquivos |
| `temas/historico.md` | Anti-repetição — tudo já publicado, nos dois canais |
| `calendarios/AAAA-SNN/` | Saída de cada semana — `calendario.md` + `linkedin/` + `instagram/` + `relatorio.md` quando gerado |

## Conformidade OAB

Cada briefing carrega, na sua seção 7, a prova de que passou pelo checklist
derivado da Cartilha do CFOAB "Principais dúvidas sobre Publicidade na
Advocacia: entendendo o Provimento 205/2021" — sem promessa de resultado,
sem caso concreto de cliente, sem CTA de conversão, sem linguagem de
urgência. Ver `docs/normas-oab.md` para o detalhe de cada regra e exemplos
de reescrita.

## LinkedIn — canal 100% B2B

Desde 2026-08-17, o LinkedIn existe para atrair empresas e reforçar o
escritório como referência técnica — não é o Instagram em texto mais longo.
Só cobre as 3 áreas inerentemente corporativas (Empresarial, Trabalhista
pelo ângulo empregador/RH, Tributário), sempre nos mesmos dias, sem
rodízio de área. 80% dos posts adotam registro de **autoridade técnica**
(análise mais profunda, comparação antes/depois da norma, framing de risco
para quem decide na empresa); 20% são **informativo direto** (mesmo tom
corporativo, mais objetivo). Ver `docs/formatos.md` para as specs completas
e `docs/perfil-escritorio.md` para o tom de voz. O checklist de
`docs/normas-oab.md` vale integralmente nos dois subtipos — autoridade se
constrói pela precisão da análise, nunca por autoelogio.

## Kanban de produção e métricas

O banco "Posts" do Notion também acompanha a produção depois da aprovação
editorial — Status com 6 etapas (Rascunho → Em aprovação → Aprovado → Em
produção → Pronto para publicar → Publicado), mais `Link da arte`, `Link do
post` e `Responsável`. E acumula métricas de desempenho (Alcance, Curtidas,
Comentários, Compartilhamentos, Salvamentos, Cliques, Taxa de engajamento),
preenchidas manualmente pelo escritório ~2 semanas após a publicação.

A cada execução semanal, a rotina verifica se há métricas novas prontas para
virar relatório (`templates/relatorio-semanal.md`) — ranking, desempenho por
área e por formato, e recomendações para o próximo ciclo, registradas em
`docs/aprendizados.md`. Essas recomendações só ajustam formato, área, tema
ou cadência — **nunca** afrouxam o checklist de conformidade OAB. Ver
`docs/notion.md` para o esquema completo e `docs/aprendizados.md` para a
trava.

## Fora de escopo

- Geração de arte/design visual — o entregável é briefing + copy.
- Publicação automática em redes sociais — a rotina para na aprovação
  (Status no Notion).
- Automação da coleta de métricas via API do Instagram/Meta — a entrada é
  manual por ora; o que seria necessário para automatizar está documentado
  em `docs/notion.md`.

## Operação

- **Rodar manualmente**: peça para o Claude Code, neste repositório, seguir
  a skill `calendario-semanal`.
- **Renovar a Routine**: Routines recorrentes podem expirar após um período
  em algumas configurações de agendamento. Verifique periodicamente se a
  Routine segue ativa (`next_run_at` no futuro) e recrie com os parâmetros
  de `PROMPT_ROTINA.md` se necessário.
