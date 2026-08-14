# Notion — IDs e esquema

Workspace: *mafe's Notion*, sob a página "Gutmann & Silva". Estes IDs já
existem e não devem ser recriados a cada execução — a Routine lê este
arquivo e publica diretamente neles.

## Estrutura existente

| Entidade | Nome | URL / ID |
|---|---|---|
| Página | Calendário Editorial | `3bb1d8cd0ae680ccad77ccddb430d0ab` |
| Database | Posts | `https://app.notion.com/p/52680f1596304f08a016a3bfa181895b` |
| Data source (Posts) | Posts | `collection://71818c42-f4bd-4c7b-8471-8ab4bfad9bdd` |
| View | Default view (tabela) | `view://405a8c53-971e-4a73-b25a-685ec55144a4` |
| View | Calendário (por Data) | `view://3bc1d8cd-0ae6-8106-a578-000cf845d306` |
| View | Aprovação (board por Status) | `view://3bc1d8cd-0ae6-8107-a32a-000c73d6c8ba` |

Sub-páginas de panorama semanal são filhas diretas de **Calendário
Editorial** (não da database), criadas uma por semana:

| Semana | Sub-página | URL |
|---|---|---|
| 2026-S34 | Semana 34 · 17–22/08 | `https://app.notion.com/p/3bc1d8cd0ae681568997df9a345a6432` |

Atualize esta tabela ao final de cada execução semanal, com append da nova
linha — não reescreva as anteriores.

## Esquema do data source "Posts"

```sql
CREATE TABLE "Posts" (
  "Tema" TITLE,
  "date:Data:start" TEXT,           -- data de publicação (ISO)
  "Semana" TEXT,                    -- ex.: "2026-S35"
  "Área" SELECT('Empresarial', 'Cível', 'Trabalhista', 'Tributário',
                 'Família', 'Previdenciário'),
  "Canal" SELECT('LinkedIn', 'Instagram'),
  "Formato" SELECT('Carrossel', 'Post estático', 'Reel', 'Stories',
                    'LinkedIn', 'Texto longo'),
  "Status" SELECT('Rascunho', 'Em aprovação', 'Aprovado', 'Publicado'),
  "Gancho" TEXT,
  "Conformidade OAB" SELECT('OK', 'Revisar')
)
```

Todas as opções de Select já existem no data source — não recriar.

`Canal` foi adicionado em 2026-08-14, junto com a opção `Texto longo` em
`Formato` (renomeação funcional de `LinkedIn`, mantida como opção legada
porque já está em uso nos registros da semana 2026-S34 — não remover).
Toda execução a partir da 2026-S35 preenche `Canal`; as 6 linhas antigas
da 2026-S34 ficaram sem esse campo (pré-existentes ao esquema de dois
calendários) e podem ser preenchidas manualmente depois, se quiser.

## Como publicar uma semana nova

1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever qualquer
   conteúdo (sintaxe do Notion Markdown tem particularidades — tabelas em
   XML, não Markdown puro; blocos de código para trechos monoespaçados
   etc.).
2. Para cada um dos 9 posts (3 LinkedIn + 6 Instagram), `notion-create-pages`
   com `parent.data_source_id = collection://71818c42-f4bd-4c7b-8471-8ab4bfad9bdd`,
   propriedades (`Tema`, `date:Data:start`, `Semana`, `Área`, `Canal`,
   `Formato`, `Status = "Em aprovação"`, `Gancho`, `Conformidade OAB`) e o
   briefing completo (8 seções do template) como `content`.
3. Criar a sub-página da semana (`notion-create-pages`,
   `parent.page_id = 3bb1d8cd0ae680ccad77ccddb430d0ab`) com o panorama da
   semana (os dois calendários, ver `templates/calendario-semanal.md`) e
   `<mention-page>` para cada um dos 9 posts criados no passo 2.
4. Não recriar database, data source nem views — eles persistem entre
   execuções.
5. Registrar a nova sub-página na tabela acima, neste arquivo, e commitar
   junto com a saída da semana.

## Observação sobre a Routine

A Routine dispara uma sessão nova a cada execução, que **não herda os
conectores desta conversa**. O conector do Notion precisa estar
explicitamente anexado à Routine (`create_trigger` com `connectors:
["Notion"]`) — do contrário a automação gera e comita tudo em `main`
normalmente, mas pula a publicação no Notion e registra isso na sub-página
e na mensagem de commit.
