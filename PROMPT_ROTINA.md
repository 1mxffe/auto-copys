# Prompt da Routine — calendário editorial semanal

Cole este texto como prompt da Routine (sexta-feira, 8h de Brasília — cron
`0 11 * * 5`, UTC). O conector **Notion** precisa estar anexado à Routine —
sessões disparadas por trigger não herdam os conectores da conversa em que
a Routine foi criada.

---

```
Gere os DOIS calendários editoriais da PRÓXIMA semana para o escritório
Gutmann & Silva — um para LinkedIn, um para Instagram — e publique no Notion.

Siga a skill `calendario-semanal` deste repositório. Ela contém o procedimento
completo; o resumo do que deve sair:

1. Calcule a próxima semana ISO (segunda a sábado) a partir da data de hoje.
2. Produza 9 posts, em dois calendários com cadência própria:
   - LinkedIn: 3 posts (segunda, quarta, sexta), sempre formato "Texto longo".
   - Instagram: 6 posts (segunda a sábado), um por área — Empresarial, Cível,
     Trabalhista, Tributário, Família, Previdenciário —, formato em rodízio.
3. Determine área×dia×formato de cada canal seguindo as matrizes de
   `docs/formatos.md` (ciclo de 3 semanas no Instagram, ciclo de 2 semanas
   de grupo de área no LinkedIn).
4. Escolha os temas em `temas/<area>.md`, sem repetir nada de
   `temas/historico.md` — a checagem de repetição vale para os dois canais
   juntos, não separadamente. Se houver acesso à web, você pode trocar uma
   pauta por assunto de atualidade jurídica relevante; se não houver, use o
   banco e siga em frente.
5. Escreva um briefing completo por post no formato de
   `templates/briefing-post.md` (incluindo o campo Canal), com a copy final
   pronta para a arte.
6. Aplique o checklist de `docs/normas-oab.md` a CADA peça, item por item. Os
   posts são informativos: sem promessa de resultado, sem honorários, sem
   casos concretos, sem linguagem de urgência ou captação, sem
   autoengrandecimento. Se uma copy não passar, reescreva antes de seguir.
   Registre o resultado do checklist no briefing.
7. Salve em `calendarios/AAAA-SNN/linkedin/` e
   `calendarios/AAAA-SNN/instagram/`, com um `calendario.md` de panorama na
   raiz da semana, e atualize `temas/historico.md`.
8. Publique no Notion usando os IDs de `docs/notion.md`: uma linha por post
   no banco "Posts" (9 linhas, campo Canal preenchido), com o briefing
   completo no corpo da página, mais a sub-página de panorama da semana com
   os dois calendários. Status inicial: "Em aprovação".
9. Comite direto na branch `main` e dê push. NÃO abra Pull Request. Faça
   `git pull origin main` antes de commitar. Mensagem do commit:
   "Calendário editorial — Semana NN/AAAA".

Se algum passo falhar, conclua todos os outros e diga explicitamente na mensagem do
commit e na sub-página do Notion o que ficou de fora e por quê — e em qual canal.
```

---

## Checklist de configuração da Routine

- [ ] `cron_expression`: `0 11 * * 5` (UTC) = 8h de Brasília
- [ ] `connectors`: `["Notion"]` — se sua organização bloquear o parâmetro
      `connectors` na criação via ferramenta, anexe manualmente pela
      interface de Routines do claude.ai depois de criar o trigger.
- [ ] `environment_id`: mesmo ambiente do repositório `1mxffe/auto-copys`
- [ ] `create_new_session_on_fire: true` (cada execução parte de sessão
      limpa — a skill já traz todo o contexto necessário)

## Renovação

Routines recorrentes podem expirar após um período em algumas configurações
de agendamento (ex.: 7 dias, a depender do plano). Verifique periodicamente
com `list_triggers` se a Routine `Calendário editorial semanal` segue
`enabled: true` e com `next_run_at` no futuro. Se estiver desabilitada ou
sem próxima execução, recrie com os mesmos parâmetros deste arquivo.
