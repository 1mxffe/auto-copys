# Templates do Figma — convenção de nomes para o plugin

Este documento é a especificação que o **designer** precisa seguir ao
criar os templates de Instagram no Figma, para que o plugin
(`figma-plugin/`) consiga encontrá-los e preencher o texto da semana
automaticamente.

> Só os 3 formatos do **Instagram** precisam de template — o LinkedIn é
> sempre "Texto longo" (só copy, sem arte, ver `docs/formatos.md`).

## Como o plugin funciona, resumido

1. Alguém do escritório abre o arquivo do Figma com os templates e roda o
   plugin.
2. O plugin digita a semana (ex.: `2026-S35`) e busca
   `calendarios/2026-S35/posts.json` direto do GitHub (branch `main`).
2. Para cada um dos 6 posts de Instagram daquela semana, o plugin acha o
   template certo pelo **nome exato do frame**, duplica, e escreve o texto
   nas **camadas de texto certas pelo nome exato da camada**.
3. O duplicado fica do lado do template original, com um nome novo — o
   template original nunca é alterado, então serve pra semana seguinte
   também.

Se um nome de frame ou de camada de texto não bater **exatamente** com o
que está abaixo, o plugin não encontra e reporta erro pra aquele post
específico (não trava os outros).

## Convenção de nomes exigida

### Post estático — 1 frame, 2 camadas de texto

- Frame: nome exato **`TEMPLATE_POST_ESTATICO`**
- Dentro dele, duas camadas de texto (nome da camada, não conteúdo):
  - **`titulo`**
  - **`corpo`**

### Carrossel — 5 frames (um por slide), 1 camada de texto cada

- 5 frames, nomes exatos **`TEMPLATE_CARROSSEL_SLIDE_1`** até
  **`TEMPLATE_CARROSSEL_SLIDE_5`**
- Dentro de cada um, uma camada de texto chamada **`texto`**

Os 5 podem ficar lado a lado no Figma, como já costuma ser feito — o
plugin trata cada um como uma peça independente (afinal, no Instagram
viram 5 imagens separadas do carrossel).

### Reel — até 4 frames (um por "tela" do roteiro), 1 camada de texto cada

- Até 4 frames, nomes exatos **`TEMPLATE_REEL_TELA_1`** até
  **`TEMPLATE_REEL_TELA_4`** (esses frames representam o texto que
  aparece na tela em cada trecho do roteiro — não o vídeo em si, que
  continua sendo editado fora do Figma)
- Dentro de cada um, uma camada de texto chamada **`texto`**
- A skill semanal, na prática, sempre gera roteiro de Reel com 4 trechos
  (`docs/formatos.md`) — se algum dia gerar mais que 4, o plugin avisa e
  ignora o excedente; menos que 4 também funciona (só usa os primeiros N).

## Onde colocar os templates no arquivo do Figma

Os 7 frames-molde (`TEMPLATE_POST_ESTATICO` + 5 do carrossel + até 4 do
reel) devem estar todos na **mesma página** do Figma, de preferência numa
página/seção chamada "Templates" — o plugin procura na página
atualmente aberta quando você roda ele, então essa precisa ser a página
ativa no momento.

## O que o plugin NÃO faz

- Não cria o template do zero — a estrutura visual (paleta, tipografia,
  logotipo, ícones) é trabalho do designer, seguindo o manual de marca e
  as recomendações de cada briefing (seção 6 de
  `templates/briefing-post.md`).
- Não exporta a imagem final (PNG/JPG) — isso continua sendo "Arquivo →
  Exportar" manual no Figma, depois de conferir visualmente o texto
  populado.
- Não preenche a legenda do post (o texto que vai na publicação do
  Instagram, fora da imagem) — isso está em `posts.json` também
  (`legenda` e `hashtags` de cada post), mas em texto puro, pra copiar
  direto de lá na hora de publicar. Ver `docs/formatos-json.md` (schema
  do `posts.json`).
- Não atualiza o campo "Link da arte" no Notion — isso continua manual,
  depois de a arte estar pronta e publicada onde o time guarda os
  arquivos (Drive, etc.).

## Testando

Depois que os templates estiverem prontos com os nomes certos:

1. `Plugins → Development → Import plugin from manifest…` e apontar para
   `figma-plugin/manifest.json` deste repositório.
2. Abrir a página com os templates, rodar o plugin, digitar uma semana
   que já tem `posts.json` gerado (ex.: `2026-S35` — ver
   `calendarios/2026-S35/posts.json`).
3. Conferir se os 6 duplicados apareceram com o texto certo.

Este plugin não foi testado dentro do Figma de verdade nesta sessão (sem
acesso ao aplicativo aqui) — a primeira rodada real de vocês é também o
primeiro teste de ponta a ponta. Qualquer nome de camada que não bater
aparece no log de erro do plugin, então dá pra ajustar rápido.
