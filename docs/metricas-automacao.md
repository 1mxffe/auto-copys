# Automação da coleta de métricas do Instagram

Este documento descreve a automação que substitui o preenchimento manual
das métricas de desempenho no banco "Posts" do Notion (Alcance, Curtidas,
Comentários, Compartilhamentos, Salvamentos — ver `docs/notion.md`).

> Este é um projeto de infraestrutura à parte da automação semanal de
> calendário (`.claude/skills/calendario-semanal/`). Ele **alimenta** o
> mesmo banco "Posts" que a skill semanal lê no passo 1, mas roda em
> agendamento próprio, via GitHub Actions — não dentro da Routine do
> calendário.

## O que fica automatizado, e o que não fica

| Campo no Notion | Automatizável via API? | Observação |
|---|---|---|
| Alcance | ✅ | `reach` — via Insights API |
| Curtidas | ✅ | `like_count` — vem no próprio objeto da mídia |
| Comentários | ✅ | `comments_count` — vem no próprio objeto da mídia |
| Compartilhamentos | ✅ | `shares` — via Insights API (não disponível para todo tipo de mídia; ver limitações) |
| Salvamentos | ✅ | `saved` — via Insights API |
| Cliques no link | ⚠️ **não automatizável para posts orgânicos** | A Graph API não expõe clique em link para post orgânico de feed/Reel/carrossel — isso só existe como métrica de anúncio (Ads Insights) ou de link de Stories (`taps_forward`/`taps_back`, que não é "clique em link"). **Este campo continua manual** ou deve ser reavaliado — ver "Decisão pendente" abaixo. |
| Taxa de engajamento | — | Já é Formula no Notion, calculada automaticamente a partir dos campos acima — nada muda aqui. |

**Decisão pendente, sua**: como o post do calendário editorial não carrega
link clicável (Instagram não permite link em legenda), o campo "Cliques
no link" provavelmente nunca teve dado real por trás — vale decidir se
ele deve (a) continuar manual para o dia em que houver link em bio
rastreável, ou (b) ser removido do schema. A automação abaixo **não
mexe nesse campo** — ele segue em branco até vocês decidirem.

## Pré-requisitos (você precisa fazer isso fora do Claude Code)

A automação depende da **Instagram Graph API** (via Meta), que exige uma
cadeia de configuração que só o dono da conta consegue fazer:

### 1. Conta do Instagram como conta profissional

A conta `@` do escritório precisa ser **Conta comercial** (Business) ou
**Criador de conteúdo**, não conta pessoal. Isso se faz no app do
Instagram: Configurações → Conta → Mudar para conta profissional.

### 2. Vincular a conta a uma Página do Facebook

A Graph API só enxerga uma conta do Instagram através de uma Página do
Facebook vinculada a ela (mesmo que a Página em si não seja usada para
nada). No Instagram: Configurações → Conta → Contas vinculadas →
Facebook. Se o escritório não tem Página do Facebook, é preciso criar
uma (gratuito, leva 2 minutos).

### 3. Criar um Meta App

Em [developers.facebook.com](https://developers.facebook.com) →
"My Apps" → "Create App" → tipo **Business**. Isso cria um `App ID` e
`App Secret`.

No painel do App, adicionar o produto **Instagram Graph API** (ou
"Instagram API with Instagram Login", dependendo da versão atual do
painel da Meta — a nomenclatura muda com frequência).

### 4. Permissões necessárias

O token de acesso precisa destes escopos:
- `instagram_basic`
- `instagram_manage_insights`
- `pages_show_list`
- `pages_read_engagement`

Para uso só do escritório (não para terceiros), a Meta costuma liberar
essas permissões em **modo de desenvolvimento/teste** sem precisar de
App Review completo, desde que o usuário que gera o token seja
administrador do App e da Página. Se em algum momento a Meta exigir App
Review para alguma dessas permissões, é um processo à parte (formulário
+ vídeo de demonstração de uso) — não é algo que a automação em si
resolve.

### 5. Gerar o token de acesso

1. No [Graph API Explorer](https://developers.facebook.com/tools/explorer/),
   selecionar o App criado, o usuário administrador, e as 4 permissões
   acima.
2. Gerar um **token de acesso de usuário** de curta duração.
3. Trocar por um **token de longa duração** (60 dias) via endpoint:
   ```
   GET https://graph.facebook.com/v21.0/oauth/access_token
     ?grant_type=fb_exchange_token
     &client_id={App ID}
     &client_secret={App Secret}
     &fb_exchange_token={token de curta duração}
   ```
4. Obter o `Instagram Business Account ID` (não é o `@usuário`, é um ID
   numérico) via:
   ```
   GET https://graph.facebook.com/v21.0/me/accounts?access_token={token}
   ```
   pega o `id` da Página, depois:
   ```
   GET https://graph.facebook.com/v21.0/{page-id}?fields=instagram_business_account&access_token={token}
   ```

**O token de longa duração expira a cada ~60 dias** e precisa ser
renovado manualmente (repetindo o passo 3 com o token atual antes que
expire) — a automação deste repositório **não renova o token sozinha**
(ver "Fora de escopo desta automação" abaixo). Recomendo colocar um
lembrete recorrente (calendário do escritório, ou uma Routine do Claude
Code do tipo "lembrete") a cada ~50 dias.

## Secrets a configurar no GitHub

Depois de ter o token e o ID da conta, configure em
`Settings → Secrets and variables → Actions` deste repositório:

| Secret | Valor |
|---|---|
| `META_ACCESS_TOKEN` | O token de longa duração do passo 5 |
| `META_IG_BUSINESS_ID` | O Instagram Business Account ID do passo 5 |
| `NOTION_API_KEY` | Token de integração interna do Notion, com acesso ao banco "Posts" (criar em notion.so/my-integrations, e compartilhar o banco "Posts" com a integração) |
| `NOTION_POSTS_DATA_SOURCE_ID` | `71818c42-f4bd-4c7b-8471-8ab4bfad9bdd` (já documentado em `docs/notion.md`) |

## Como a sincronização funciona

Workflow: `.github/workflows/sync-metricas-instagram.yml`, agendado
semanalmente. Roda `scripts/sync_metricas_instagram.py`, que:

1. Consulta o Notion: posts com `Canal = Instagram`, `Status =
   "Publicado"`, campo `Link do post` preenchido, e publicados nos
   últimos 45 dias (métrica de post muito antigo já estabilizou —
   não vale gastar chamada de API nele toda semana).
2. Busca a lista de mídias recentes da conta via
   `GET /{ig-business-id}/media?fields=id,permalink`, e casa cada
   `Link do post` do Notion com o `id` da mídia correspondente pelo
   `permalink` — **não é preciso guardar o ID da mídia manualmente em
   lugar nenhum**, o link que já é preenchido na publicação basta.
3. Para cada mídia casada, busca `like_count`, `comments_count` (do
   próprio objeto) e `reach`, `saved`, `shares` (via
   `/{media-id}/insights`).
4. Atualiza a página correspondente no Notion com os 5 campos
   automatizáveis (`Cliques no link` fica intocado).
5. Loga um resumo (quantos posts casados, quantos atualizados, quantos
   sem link ainda) — visível na aba Actions do GitHub.

## Limitações conhecidas

- **Reels/vídeo**: o nome da métrica de alcance pode variar
  (`reach` vs. métricas específicas de vídeo, a depender da versão da
  API vigente quando isto rodar pela primeira vez) — o script trata
  isso com uma lista de fallback, mas vale conferir o primeiro resultado
  real contra o Instagram Insights manualmente.
- **Posts muito recentes** (< 24h): a Graph API pode retornar `reach`
  zerado ou incompleto antes de o Instagram consolidar o número — não é
  bug do script.
- **Token expira a cada ~60 dias** (ver acima) — quando expirar, o
  workflow passa a falhar com erro de autenticação; a aba Actions do
  GitHub mostra isso claramente.

## Fora de escopo desta automação

- Renovação automática do token de longa duração (exigiria dar ao
  workflow permissão de escrita nos Secrets do repositório — superfície
  de risco maior do que o benefício, para um token que expira só a cada
  ~60 dias). Renovação continua manual, seguindo o passo 5 acima.
- App Review completo junto à Meta, caso a Meta exija em algum momento
  para as permissões usadas — decisão e processo de responsabilidade do
  escritório, não algo que o código deste repositório resolve.
- Cliques no link (ver tabela acima) — sem fonte de dado real disponível
  para o formato de post atual.
