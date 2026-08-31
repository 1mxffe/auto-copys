# SDR — Reuniões e Contatos (Notion)

Sistema à parte do calendário editorial: dá ao SDR do escritório uma base de
contatos (leads) e uma agenda de reuniões marcadas, dentro do mesmo workspace
Notion (*mafe's Notion*), como página irmã de **Calendário Editorial** sob
**Gutmann & Silva**. Não tem relação funcional com `calendarios/`, `temas/`
nem com a database "Posts" — só compartilha o workspace.

Estes IDs já existem e não devem ser recriados — qualquer automação futura
deve ler este arquivo e publicar diretamente neles.

## Estrutura existente

| Entidade | Nome | URL / ID |
|---|---|---|
| Página-pai | Gutmann & Silva | `3b51d8cd0ae6801f9e71c54e031c33ef` |
| Página | SDR — Reuniões e Contatos | `https://app.notion.com/p/3cd1d8cd0ae68128a5f4dc1e6f4959f8` |
| Database | Contatos | `https://app.notion.com/p/3f9b680e8e884c30a6c23515eaad491a` |
| Data source (Contatos) | Contatos | `collection://eb089327-e769-4651-a61d-e3a4ca2292a3` |
| View (Contatos) | Default view (tabela) | criada automaticamente |
| View (Contatos) | Funil (por Status) — board | `view://3cd1d8cd-0ae6-8128-8bf9-000ca88faa7e` |
| Database | Reuniões | `https://app.notion.com/p/ab78c8cc9c1a494e8d09edd383d204ef` |
| Data source (Reuniões) | Reuniões | `collection://c5253c82-aed9-4391-8034-7d4eb926a88d` |
| View (Reuniões) | Default view (tabela) | criada automaticamente |
| View (Reuniões) | Agenda — calendário (por Data e hora) | `view://3cd1d8cd-0ae6-8140-99cf-000c0c2e2c17` |
| View (Reuniões) | Por Status — board | `view://3cd1d8cd-0ae6-8123-ac7a-000c12651045` |

Ambas as databases foram criadas como página cheia (`inline=false`), mesmo
padrão da database "Posts" do calendário editorial — aparecem como
sub-páginas dentro de **SDR — Reuniões e Contatos**.

## Esquema do data source "Contatos"

```sql
CREATE TABLE "Contatos" (
  "Nome" TITLE,
  "Empresa" TEXT,
  "Cargo" TEXT,
  "E-mail" EMAIL,
  "Telefone" PHONE_NUMBER,
  "Área de interesse" SELECT('Empresarial', 'Cível', 'Trabalhista',
                              'Tributário', 'Previdenciário'),
  "Origem do lead" SELECT('Indicação', 'Site', 'LinkedIn', 'Evento',
                           'Outbound', 'Outro'),
  "Status do lead" SELECT('Novo', 'Qualificando', 'Reunião marcada',
                           'Cliente', 'Perdido'),
  "SDR responsável" TEXT,   -- texto simples, mesma razão do "Responsável"
                            -- em Posts: não depende de todo SDR estar
                            -- cadastrado como membro do workspace Notion
  "Notas" TEXT
)
```

`Área de interesse` usa as 5 áreas do escritório (Cível aqui não se
subdivide em subtemas — isso é particularidade do calendário editorial,
não da qualificação de lead).

## Esquema do data source "Reuniões"

```sql
CREATE TABLE "Reuniões" (
  "Assunto" TITLE,
  "Contato" RELATION('Contatos', DUAL 'Reuniões'),  -- two-way: cada
                                                      -- Contato lista suas
                                                      -- Reuniões
  "date:Data e hora:start" TEXT,   -- data/hora da reunião (ISO, com hora)
  "Status" SELECT('Marcada', 'Confirmada', 'Realizada', 'Remarcada',
                   'No-show', 'Cancelada'),
  "Link da reunião" URL,           -- Google Meet / Zoom / Teams
  "Advogado responsável" TEXT,     -- quem do escritório conduz a reunião
  "SDR responsável" TEXT,          -- quem marcou/está acompanhando
  "Resultado / próximos passos" TEXT  -- preenchido pela SDR após a reunião
)
```

Todas as opções de Select já existem nos data sources — não recriar.

## Como usar

1. **Novo lead** → `notion-create-pages` em
   `parent.data_source_id = collection://eb089327-e769-4651-a61d-e3a4ca2292a3`,
   com `Status do lead = "Novo"` e `Origem do lead` preenchido. `Área de
   interesse` e `Cargo` quando já souber; senão deixar em branco e
   completar ao qualificar.
2. **Marcar reunião** → `notion-create-pages` em
   `parent.data_source_id = collection://c5253c82-aed9-4391-8034-7d4eb926a88d`,
   com `Contato` apontando para a página do lead (relation), `Status =
   "Marcada"`, `date:Data e hora:start` preenchido. Ao marcar a reunião,
   atualizar também `Status do lead` do Contato para `"Reunião marcada"`.
3. **Depois da reunião** → atualizar `Status` (`Realizada`, `Remarcada`,
   `No-show` ou `Cancelada`) e preencher `Resultado / próximos passos`. Se
   o lead virou cliente ou saiu do funil, atualizar `Status do lead` no
   Contato correspondente (`Cliente` ou `Perdido`).
4. Não recriar database, data source nem views — eles persistem entre
   execuções, mesmo padrão do database "Posts" (ver `docs/notion.md`).

## Fora de escopo (por ora)

- Integração automática de calendário (Google Calendar/Outlook) para criar
  o evento a partir da página de Reunião — hoje é manual, a SDR cria a
  reunião no Notion e o evento de calendário à parte.
- Automação de qualquer etapa deste fluxo por Routine — diferente do
  calendário editorial, este sistema não tem, por ora, nenhuma automação
  disparando sozinha; toda escrita é manual ou sob pedido explícito.
