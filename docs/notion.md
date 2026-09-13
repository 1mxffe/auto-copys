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
| 2026-S36 | Semana 36 · 31/08–05/09 | `https://app.notion.com/p/3c81d8cd0ae681749667d86af5acdd30` |
| 2026-S38 (esquema concorrente, 4 dias) | Semana 38 · 14–19/09 | `https://app.notion.com/p/3d41d8cd0ae68170ae29cd8f03b22659` |
| 2026-S38 (rascunho de teste desta automação, 5 dias) | Semana 38 (proposta alternativa · 5 dias) · 14–18/09 | `https://app.notion.com/p/3da1d8cd0ae681bf9cdee82571d3f76f` |

Atualize esta tabela ao final de cada execução semanal, com append da nova
linha — não reescreva as anteriores.

**⚠️ Duas linhas de trabalho conflitantes para a Semana 38, registradas
em 2026-09-13**: uma branch nunca mesclada em `main`
(`claude/instagram-editorial-calendar-notion-6ku7nf`, commit `95d3c39`,
decidida em 2026-09-03) construiu um esquema diferente — Instagram de 4
dias, 1 dia fixo de "Isenção de IR" (só quinta), ciclo de área de 4
semanas, contador global de 3 formatos, banco em `temas/isencao-ir.md` e
`docs/produto-isencao-ir.md`. Uma sessão usando essa branch publicou a
"Semana 38 · 14–19/09" direto no Notion (sem conseguir dar push ao
GitHub). O PR [#6](https://github.com/1mxffe/auto-copys/pull/6) (branch
`claude/affectionate-brown-1cn6xj`, decisão de 2026-09-12/13, é o que este
arquivo documenta a partir daqui) construiu, em paralelo e sem
conhecimento disso, um esquema diferente — Instagram de 5 dias, 2 dias
fixos, ciclo de 5 semanas, 6 formatos por trilha. Decisão explícita do
usuário: manter o esquema do PR #6 como o vigente; a página antiga não foi
apagada nem arquivada, as duas coexistem no Notion por enquanto.

Sub-páginas de relatório de métricas são criadas do mesmo jeito, uma por
semana analisada (só quando houver métrica pendente — ver skill, passos 1-2):

| Semana analisada | Sub-página | URL |
|---|---|---|
| _nenhuma ainda_ | | |

Atualize esta tabela junto com a anterior, com append — mesma regra.

## Esquema do data source "Posts"

**Corrigido em 2026-09-13 para bater com o schema real ao vivo** (conferido
via `notion-fetch` na `collection://71818c42-f4bd-4c7b-8471-8ab4bfad9bdd`
— a versão anterior deste arquivo tinha uma propriedade "Semana" que nunca
existiu no banco real, um Status desatualizado, e não sabia que `Área` já
tinha "Isenção de IR" como opção própria):

```sql
CREATE TABLE "Posts" (
  "Tema" TITLE,
  "date:Data:start" TEXT,           -- data de publicação (ISO)
  "Área" SELECT('Empresarial', 'Cível', 'Trabalhista', 'Tributário',
                 'Família', 'Previdenciário', 'Isenção de IR'),
  "Canal" SELECT('LinkedIn', 'Instagram'),
  "Formato" SELECT('Carrossel', 'Carrossel curto', 'Carrossel aprofundado',
                    'Post estático', 'Reel', 'Reel rápido', 'Stories',
                    'LinkedIn', 'Texto longo'),
  "Status" SELECT('Rascunho', 'Briefings', 'Em produção',
                   'Pronto para publicar',
                   'Criação das artes/Edição dos vídeos', 'Gravação',
                   'Aprovação Dr. Cris', 'Aprovação advogado da área',
                   'Publicado'),
  "Gancho" TEXT,
  "Conformidade OAB" SELECT('OK', 'Revisar'),

  -- Kanban de produção
  "Link da arte" URL,                -- Canva/Figma/Drive
  "Link do post" URL,                -- link do post no ar, preenchido em "Publicado"
  "Responsável" TEXT,                -- quem está produzindo a arte desta peça
  "Advogado Responsavel" TEXT,       -- advogado que revisa/aprova juridicamente a peça

  -- Métricas de desempenho (preenchimento manual)
  "Alcance" NUMBER,
  "Curtidas" NUMBER,
  "Comentários" NUMBER,
  "Compartilhamentos" NUMBER,
  "Salvamentos" NUMBER,
  "Taxa de engajamento" FORMULA      -- (Curtidas+Comentários+Compartilhamentos+Salvamentos)/Alcance
)
```

**Não existe propriedade "Semana"** — nunca existiu no banco real, apesar
de versões anteriores deste arquivo (e do template do briefing) mencionarem
uma. Registre a semana só no texto da página (título/conteúdo), não numa
propriedade. **Não existe "Cliques no link"** — só os 5 campos de
engajamento acima.

`Status` **não tem** "Em aprovação" nem "Aprovado" (diferente do que este
arquivo dizia antes) — o pipeline real vai de `Rascunho` até `Publicado`
passando por etapas de produção de arte/vídeo e duas aprovações
específicas (Dr. Cris, depois advogado da área). Ao criar um post novo
via automação, use `Status = "Rascunho"`.

`Área` **já tem `'Isenção de IR'` como opção própria** — não é "Tributário"
como versões anteriores deste arquivo (e de `docs/formatos.md`,
`CLAUDE.md`) assumiam. Use `Área = "Isenção de IR"` para os posts de
terça/quinta do Instagram.

A maioria das opções de Select já existe no data source — não recriar.
**Exceção histórica**: `Carrossel curto`, `Carrossel aprofundado` e `Reel
rápido` (Formato) foram criadas em 2026-09-13, via
`notion-update-data-source`, ao publicar a primeira semana sob o esquema
de 6 formatos (ver `docs/formatos.md`, "Os formatos do Instagram") — já
existem no Select, não recriar de novo.

`Carrossel` (Select) segue representando o formato "Carrossel padrão" (5
slides) e `Reel` segue representando "Reel aprofundado" (30-45s) — os
nomes internos do Select não foram renomeados para não invalidar as
páginas já publicadas (S34-S36); a distinção de 3 níveis de Carrossel e 2
de Reel existe só nos nomes usados pela documentação e pelo briefing (ver
`docs/formatos.md`), mapeados para os valores de Select como segue: Carrossel
curto → `Carrossel curto`; Carrossel padrão → `Carrossel`; Carrossel
aprofundado → `Carrossel aprofundado`; Reel rápido → `Reel rápido`; Reel
aprofundado → `Reel`.

`Canal` foi adicionado em 2026-08-14, junto com a opção `Texto longo` em
`Formato` (renomeação funcional de `LinkedIn`). As opções `Stories` e
`LinkedIn` (Formato) ficam mantidas como legado no Select mesmo sem uso —
remover uma opção em uso é destrutivo para as páginas que a usam. Toda
execução a partir da 2026-S34 (regenerada em 2026-08-14 sob o esquema de
dois calendários) preenche `Canal`.

`Família`, em `Área`, é a mesma situação desde 2026-08-26: a opção fica
mantida no Select como legado (páginas antigas a usam), mas nenhuma
execução nova a atribui — Família virou subtema de Cível (banco em
`temas/civel/familia.md`), e posts sobre esse subtema levam `Área =
"Cível"`, com o subtema anotado no título (`Tema`) da página, não numa
propriedade própria (ver `docs/formatos.md`, seção "Cível — subtemas").

**Isenção de Imposto de Renda** (terça e quinta do Instagram, desde
2026-09-12), diferente de Família: **usa a opção própria `Área = "Isenção
de IR"`**, que já existe no Select ao vivo (corrigido em 2026-09-13 — ver
nota acima). O ângulo específico (ex.: "Isenção de Imposto de Renda —
doença grave...") vai no título (`Tema`) da página, além da própria opção
de Área já indicar o recorte.

`Responsável` é campo de texto simples (não Pessoa/People) para não
depender de todo o time estar cadastrado como membro do workspace Notion.
`Advogado Responsavel` (também texto simples, sem acento no nome da
propriedade) é distinto — registra quem faz a revisão jurídica da peça,
usado pelas etapas "Aprovação Dr. Cris" e "Aprovação advogado da área" do
`Status`.

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
2. Para cada um dos 8 posts (3 LinkedIn + 5 Instagram), `notion-create-pages`
   com `parent.data_source_id` = o UUID puro da data source (sem o prefixo
   `collection://` — o parser da API rejeita esse prefixo), propriedades
   (`Tema`, `date:Data:start`, `Área`, `Canal`, `Formato`, `Status =
   "Rascunho"`, `Gancho`, `Conformidade OAB`) e o briefing completo como
   `content`. Não existe propriedade `Semana` — mencione a semana só no
   texto. Deixe os campos de kanban (`Link da arte`, `Link do post`,
   `Responsável`, `Advogado Responsavel`) e de métrica (`Alcance`,
   `Curtidas`, `Comentários`, `Compartilhamentos`, `Salvamentos`) em
   branco — são preenchidos depois, manualmente, conforme a peça avança no
   pipeline real (`Status`) e o post acumula resultado.
3. Criar a sub-página da semana (`notion-create-pages`,
   `parent.page_id = 3bb1d8cd0ae680ccad77ccddb430d0ab`) com o panorama da
   semana (os dois calendários, ver `templates/calendario-semanal.md`) e
   `<mention-page>` para cada um dos 8 posts criados no passo 2.
4. Não recriar database, data source nem views — eles persistem entre
   execuções.
5. Registrar a nova sub-página na tabela acima, neste arquivo, e commitar
   junto com a saída da semana.

## Como publicar o relatório de métricas (passo 2 da skill)

1. Ler as propriedades de métrica dos 8 posts da semana analisada
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
