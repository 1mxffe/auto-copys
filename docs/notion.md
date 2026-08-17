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
| View | Produção (board por Status, 6 etapas — renomeada de "Aprovação" em 2026-08-14) | `view://3bc1d8cd-0ae6-8107-a32a-000c73d6c8ba` |

Sub-páginas de panorama semanal são filhas diretas de **Calendário
Editorial** (não da database), criadas uma por semana:

| Semana | Sub-página | URL |
|---|---|---|
| 2026-S34 | Semana 34 · 17–22/08 | `https://app.notion.com/p/3bc1d8cd0ae681568997df9a345a6432` |
| 2026-S35 | Semana 35 · 24–29/08 | `https://app.notion.com/p/3bf1d8cd0ae681f8a6f1c85e797f0b54` |

Atualize esta tabela ao final de cada execução semanal, com append da nova
linha — não reescreva as anteriores.

Sub-páginas de relatório de métricas são criadas do mesmo jeito, uma por
semana analisada (só quando houver métrica pendente — ver skill, passos 1-2):

| Semana analisada | Sub-página | URL |
|---|---|---|
| _nenhuma ainda_ | | |

Atualize esta tabela junto com a anterior, com append — mesma regra.

## Esquema do data source "Posts"

```sql
CREATE TABLE "Posts" (
  "Tema" TITLE,
  "date:Data:start" TEXT,           -- data de publicação (ISO)
  "Semana" TEXT,                    -- ex.: "2026-S34"
  "Área" SELECT('Empresarial', 'Cível', 'Trabalhista', 'Tributário',
                 'Família', 'Previdenciário'),
  "Canal" SELECT('LinkedIn', 'Instagram'),
  "Formato" SELECT('Carrossel', 'Post estático', 'Reel', 'Stories',
                    'LinkedIn', 'Texto longo'),
  "Status" SELECT('Rascunho', 'Em aprovação', 'Aprovado', 'Em produção',
                   'Pronto para publicar', 'Publicado'),
  "Gancho" TEXT,
  "Conformidade OAB" SELECT('OK', 'Revisar'),

  -- Kanban de produção (adicionado em 2026-08-14)
  "Link da arte" URL,                -- Canva/Figma/Drive, preenchido em "Em produção"
  "Link do post" URL,                -- link do post no ar, preenchido em "Publicado"
  "Responsável" TEXT,                -- quem está produzindo a arte desta peça

  -- Métricas de desempenho (adicionado em 2026-08-14, preenchimento manual)
  "Alcance" NUMBER,
  "Curtidas" NUMBER,
  "Comentários" NUMBER,
  "Compartilhamentos" NUMBER,
  "Salvamentos" NUMBER,
  "Cliques no link" NUMBER,
  "Taxa de engajamento" FORMULA      -- (Curtidas+Comentários+Compartilhamentos+Salvamentos)/Alcance
)
```

Todas as opções de Select já existem no data source — não recriar.

`Canal` foi adicionado em 2026-08-14, junto com a opção `Texto longo` em
`Formato` (renomeação funcional de `LinkedIn`). As opções `Stories` e
`LinkedIn` (Formato) ficam mantidas como legado no Select mesmo sem uso —
remover uma opção em uso é destrutivo para as páginas que a usam. Toda
execução a partir da 2026-S34 (regenerada em 2026-08-14 sob o esquema de
dois calendários) preenche `Canal`.

`Status` ganhou duas etapas novas na mesma data ("Em produção", "Pronto para
publicar") — o board "Produção" passou a cobrir o pipeline inteiro, do
briefing ao post no ar, não só a aprovação editorial. `Responsável` é campo
de texto simples (não Pessoa/People) para não depender de todo o time estar
cadastrado como membro do workspace Notion.

**Métricas — entrada manual por ora.** Sem conector de Instagram/Meta
disponível neste ambiente, a coleta é manual: o escritório olha o Instagram
Insights e preenche os 6 campos numéricos direto na linha do post,
tipicamente ~2 semanas após a publicação (tempo de o número estabilizar).
`Taxa de engajamento` é uma Formula, calculada automaticamente a partir dos
outros campos — não preencher manualmente.

*Caminho de automação futura (não construído agora):* a coleta poderia ser
automatizada via Instagram Graph API, o que exigiria (1) um Meta App
registrado e, para certas permissões, revisado pela Meta; (2) a conta do
Instagram como conta profissional vinculada a uma Página do Facebook; (3) um
token de acesso de longa duração, que expira e precisa ser renovado a cada
~60 dias. É um projeto de infraestrutura à parte — decisão editorial
explícita do usuário, não algo a construir dentro desta automação.

## Como publicar uma semana nova

1. Ler `notion://docs/enhanced-markdown-spec` antes de escrever qualquer
   conteúdo (sintaxe do Notion Markdown tem particularidades — tabelas em
   XML, não Markdown puro; blocos de código para trechos monoespaçados
   etc.).
2. Para cada um dos 9 posts (3 LinkedIn + 6 Instagram), `notion-create-pages`
   com `parent.data_source_id = collection://71818c42-f4bd-4c7b-8471-8ab4bfad9bdd`,
   propriedades (`Tema`, `date:Data:start`, `Semana`, `Área`, `Canal`,
   `Formato`, `Status = "Em aprovação"`, `Gancho`, `Conformidade OAB`) e o
   briefing completo (8 seções do template) como `content`. Deixe os campos
   de kanban (`Link da arte`, `Link do post`, `Responsável`) e de métrica
   (`Alcance`, `Curtidas`, `Comentários`, `Compartilhamentos`,
   `Salvamentos`, `Cliques no link`) em branco — são preenchidos depois,
   manualmente, conforme a peça avança na produção e o post acumula
   resultado.
3. Criar a sub-página da semana (`notion-create-pages`,
   `parent.page_id = 3bb1d8cd0ae680ccad77ccddb430d0ab`) com o panorama da
   semana (os dois calendários, ver `templates/calendario-semanal.md`) e
   `<mention-page>` para cada um dos 9 posts criados no passo 2.
4. Não recriar database, data source nem views — eles persistem entre
   execuções.
5. Registrar a nova sub-página na tabela acima, neste arquivo, e commitar
   junto com a saída da semana.

## Como publicar o relatório de métricas (passo 2 da skill)

1. Ler as propriedades de métrica dos 9 posts da semana analisada
   (`notion-query-database-view` ou `notion-fetch` sobre a página de cada
   post) — nunca recalcular `Taxa de engajamento` manualmente, é Formula.
2. Escrever `calendarios/AAAA-SNN/relatorio.md` a partir de
   `templates/relatorio-semanal.md`.
3. Criar a sub-página do relatório (`notion-create-pages`,
   `parent.page_id = 3bb1d8cd0ae680ccad77ccddb430d0ab`), título
   `Relatório · Semana NN` — irmã da sub-página "Semana NN" daquela mesma
   semana.
4. Append das recomendações em `docs/aprendizados.md`.

## Observação sobre a Routine

A Routine dispara uma sessão nova a cada execução, que **não herda os
conectores desta conversa**. O conector do Notion precisa estar
explicitamente anexado à Routine (`create_trigger` com `connectors:
["Notion"]`) — do contrário a automação gera e comita tudo em `main`
normalmente, mas pula a publicação no Notion e registra isso na sub-página
e na mensagem de commit.
