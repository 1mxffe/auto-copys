# Calendário editorial — Semana 36/2026 (31/08–05/09)

Panorama da semana, nos dois canais. Cada linha resume um briefing
completo — o detalhe está no arquivo individual da pasta do canal.

## LinkedIn (3 posts)

| Dia | Área | Formato | Subtipo | Tema | Arquivo | Conformidade OAB |
|---|---|---|---|---|---|---|
| Segunda 31/08 | Empresarial | Texto longo | Autoridade técnica | Compliance e programas de integridade — por que empresas de médio porte já são cobradas por isso | `linkedin/01-segunda-empresarial.md` | ✅ |
| Quarta 02/09 | Trabalhista | Texto longo | Autoridade técnica | Assédio moral no trabalho — o que a empresa precisa observar | `linkedin/02-quarta-trabalhista.md` | ✅ |
| Sexta 04/09 | Tributário | Texto longo | Informativo direto | Substituição tributária no ICMS — o que muda para o comércio | `linkedin/03-sexta-tributario.md` | ✅ |

## Instagram (6 posts)

| Dia | Área | Formato | Tema | Arquivo | Conformidade OAB |
|---|---|---|---|---|---|
| Segunda 31/08 | Empresarial | Reel | Dissolução de sociedade — causas e etapas | `instagram/01-segunda-empresarial.md` | ✅ |
| Terça 01/09 | Cível | Carrossel | Vizinhança e condomínio — regras básicas de convivência | `instagram/02-terca-civel.md` | ✅ |
| Quarta 02/09 | Trabalhista | Post estático | Rescisão de contrato de trabalho — tipos e o que cada um garante | `instagram/03-quarta-trabalhista.md` | ✅ |
| Quinta 03/09 | Tributário | Reel | ITCMD em heranças e doações — regras gerais por estado | `instagram/04-quinta-tributario.md` | ✅ |
| Sexta 04/09 | Família | Carrossel | Guarda compartilhada — como funciona na prática | `instagram/05-sexta-familia.md` | ✅ |
| Sábado 05/09 | Previdenciário | Post estático | Auxílio-doença — como funciona o pedido ao INSS | `instagram/06-sabado-previdenciario.md` | ✅ |

Ciclo de formato do Instagram: semana 3 do ciclo de 3 semanas
(`((36 - 34) mod 3) + 1 = 3` — ver `docs/formatos.md`).

Contador de LinkedIn (para o subtipo de registro): 6 posts publicados
antes desta semana → os 3 novos posts ocupam as posições 7, 8 e 9 do
contador (`mod 5` = 2, 3, 4) → Autoridade técnica, Autoridade técnica,
Informativo direto, nesta ordem cronológica.

## Fonte dos temas

- Todos os 9 posts: Banco de temas (`temas/<area>.md`). Nesta execução
  não houve acesso à web disponível na sessão — a rotina seguiu o banco
  normalmente, conforme `CLAUDE.md` ("rede é opcional, nunca
  bloqueante").
- Empresarial (LinkedIn) e Empresarial (Instagram) usam temas distintos
  do banco (itens 4 e 5, respectivamente), como exige a regra de
  anti-repetição por tema entre canais.
- Trabalhista (LinkedIn) e Trabalhista (Instagram) usam temas distintos
  (itens 4 e 2, respectivamente) — o item 4 (assédio moral, risco alto
  no banco) foi ajustado para ângulo de prevenção/gestão de risco da
  empresa no LinkedIn, ver seção 2 do briefing correspondente.
- Tributário (LinkedIn) e Tributário (Instagram) usam temas distintos
  (itens 6 e 5, respectivamente).
- Família (item 3, guarda compartilhada) é risco alto no banco — ajuste
  de ângulo aplicado, ver seção 2 do briefing.

## Publicação no Notion

- Página: Calendário Editorial (`3bb1d8cd0ae680ccad77ccddb430d0ab`)
- Banco "Posts": 9 linhas criadas (3 Canal=LinkedIn, 6 Canal=Instagram),
  status inicial "Em aprovação"
- Sub-página da semana: ver `docs/notion.md` (tabela de sub-páginas,
  atualizada nesta mesma execução)

## Pendências / o que ficou de fora

- Nenhuma. Execução manual, disparada porque a Routine automática
  (agendada para segunda-feira, `0 11 * * 1` UTC) não gerou a Semana
  2026-S36 apesar de `last_fired_at` registrar disparo em 2026-08-24 —
  nenhum commit correspondente foi encontrado no repositório. Esta
  execução cobre a lacuna e segue o fluxo normal da skill
  `calendario-semanal` do zero (passo 1 ao 13).
