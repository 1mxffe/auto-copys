# Prompt da Routine — calendário editorial semanal

Cole este texto como prompt da Routine (sexta-feira, 8h, `0 8 * * 5`). O
conector **Notion** precisa estar anexado à Routine — sessões disparadas por
trigger não herdam os conectores da conversa em que a Routine foi criada.

---

```
Gere o calendário editorial da PRÓXIMA semana para o escritório Gutmann & Silva
e publique no Notion.

Siga a skill `calendario-semanal` deste repositório. Ela contém o procedimento
completo; o resumo do que deve sair:

1. Calcule a próxima semana ISO (segunda a sábado) a partir da data de hoje.
2. Produza 6 posts, um por área e por dia:
   Empresarial, Cível, Trabalhista, Tributário, Família e Previdenciário.
3. Escolha os temas em `temas/<area>.md`, respeitando o rodízio de formatos de
   `docs/formatos.md` e sem repetir nada de `temas/historico.md`. Se houver acesso
   à web, você pode trocar uma pauta por assunto de atualidade jurídica relevante;
   se não houver, use o banco e siga em frente.
4. Escreva um briefing completo por post no formato de `templates/briefing-post.md`,
   com a copy final pronta para a arte.
5. Aplique o checklist de `docs/normas-oab.md` a CADA peça, item por item. Os posts
   são informativos: sem promessa de resultado, sem honorários, sem casos concretos,
   sem linguagem de urgência ou captação, sem autoengrandecimento. Se uma copy não
   passar, reescreva antes de seguir. Registre o resultado do checklist no briefing.
6. Salve em `calendarios/AAAA-SNN/` e atualize `temas/historico.md`.
7. Publique no Notion usando os IDs de `docs/notion.md`: uma linha por post no banco
   "Posts", com o briefing completo no corpo da página, mais a sub-página de panorama
   da semana. Status inicial: "Em aprovação".
8. Comite direto na branch `main` e dê push. NÃO abra Pull Request. Faça
   `git pull origin main` antes de commitar. Mensagem do commit:
   "Calendário editorial — Semana NN/AAAA".

Se algum passo falhar, conclua todos os outros e diga explicitamente na mensagem do
commit e na sub-página do Notion o que ficou de fora e por quê.
```

---

## Checklist de configuração da Routine

- [ ] `cron_expression`: `0 8 * * 5`
- [ ] `connectors`: `["Notion"]`
- [ ] `environment_id`: mesmo ambiente do repositório `1mxffe/auto-copys`
- [ ] `create_new_session_on_fire: true` (cada execução parte de sessão
      limpa — a skill já traz todo o contexto necessário)

## Renovação

Routines recorrentes podem expirar após um período em algumas configurações
de agendamento (ex.: 7 dias, a depender do plano). Verifique periodicamente
com `list_triggers` se a Routine `Calendário editorial semanal` segue
`enabled: true` e com `next_run_at` no futuro. Se estiver desabilitada ou
sem próxima execução, recrie com os mesmos parâmetros deste arquivo.
