# Canais, formatos e rodízio

## Canais e cadência

O escritório mantém **dois calendários editoriais separados**, cada um com
cadência própria — não é mais um único calendário de 6 posts:

| Canal | Posts/semana | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" (sem rodízio) |
| Instagram | 5 | Segunda, terça, quarta, quinta e sexta (sem sábado) | Rodízio entre 6 formatos (ver "Os formatos do Instagram") |

Desde 2026-08-26 até 2026-09-11 o Instagram publicava segunda a quinta e
sábado (sem sexta). **Desde 2026-09-12** o dia que sai é o sábado e o que
entra é a sexta — decisão editorial explícita do usuário, junto com a
mudança descrita abaixo. O volume total da semana continua 8 posts (3
LinkedIn + 5 Instagram).

**Também desde 2026-09-12**, o Instagram deixou de ter um dia fixo por
área em todos os 5 dias. Agora:
- **Segunda, quarta e sexta** rotacionam entre as 5 áreas (ver "Instagram —
  rodízio de área" abaixo) — sem dia fixo por área.
- **Terça e quinta** são sempre "Isenção de Imposto de Renda" — conteúdo
  fixo, banco próprio (ver "Terça e quinta — Isenção de Imposto de Renda"
  abaixo).

Motivo: variar o que aparece em cada área ao longo do tempo (em vez de
"toda terça é sempre Cível"), e dar peso extra, duas vezes por semana, a um
tema de alto interesse de busca (isenção de IR) sem esgotar o banco geral
de Tributário.

"Site institucional" segue listado como canal da marca em
`docs/perfil-escritorio.md`, mas não tem formato nem calendário definidos
nesta automação — fora de escopo até ser desenhado à parte.

Cada canal gera sua própria pasta de saída dentro da mesma semana:
`calendarios/AAAA-SNN/linkedin/` e `calendarios/AAAA-SNN/instagram/` (ver
`.claude/skills/calendario-semanal/SKILL.md`).

## Os formatos do Instagram (desde 2026-09-13: 6 formatos)

Até 2026-09-12 o Instagram girava entre só 3 formatos (Carrossel, Post
estático, Reel). Desde 2026-09-13, por pedido explícito do usuário para
variar mais o tipo de conteúdo, o rodízio tem **6 formatos** — duas
variações de Carrossel e duas de Reel, além de Post estático:

| Família | Formato | Extensão |
|---|---|---|
| Carrossel | Carrossel curto | 3 slides |
| Carrossel | Carrossel padrão | 5 slides |
| Carrossel | Carrossel aprofundado | 7 slides |
| Estático | Post estático | card único |
| Vídeo | Reel rápido | 12–15 segundos |
| Vídeo | Reel aprofundado | 30–45 segundos |

No Notion, o valor do Select `Formato` de Carrossel padrão continua
`Carrossel` e o de Reel aprofundado continua `Reel` — reaproveita os
valores já usados por S34-S36; os outros 3 são opções novas no Select
(ver `docs/notion.md`, seção do esquema "Posts").

### Regra transversal: número de lei/artigo/decisão só na legenda

**Desde 2026-09-13**, por pedido do usuário: slide de carrossel, card de
post estático e texto de tela de Reel **nunca citam número de lei, artigo
ou nome/ano de decisão** — só a ideia em linguagem acessível, fácil de
entender rápido. Precisão técnica não desaparece, ela migra inteira para
a **legenda** (ver "Legenda do Instagram" abaixo), que é onde o
aprofundamento acontece. Isso vale para os 5 formatos visuais desta
seção; o LinkedIn Texto longo não muda — lá a citação precisa continua no
corpo do texto (ver "O formato do LinkedIn" abaixo), porque não existe
card/legenda separados nesse canal.

### Carrossel curto
- **Extensão**: 3 slides.
- **Estrutura fixa**: gancho → informação central → fechamento sóbrio.
- **Entrega**: texto dos 3 slides + legenda.
- **Quando usar**: o tema cabe inteiro numa ideia só, sem precisar do
  desenvolvimento do carrossel padrão — uma regra específica, um mito, uma
  atualização pontual.
- **O que a copy precisa entregar**: direto ao ponto, sem slide de
  contexto "de aquecimento" — o slide 1 já é o gancho (ver
  `docs/perfil-escritorio.md`, "Gancho magnético"), o slide 3 já fecha.

### Carrossel padrão
- **Extensão**: 5 slides.
- **Estrutura fixa**: capa/gancho → identificação (o que é / por que
  importa) → informação-chave → aprofundamento → encerramento sóbrio.
- **Entrega**: texto de cada um dos 5 slides + legenda de publicação.
- **O que a copy precisa entregar**: cada slide deve fazer sentido lido
  isoladamente (usuário desliza rápido), mas a sequência tem que fechar uma
  ideia completa até o slide 5. Curto por slide: até ~20 palavras além do
  gancho/título — se um slide precisa de mais que isso, é sinal de que o
  tema pede carrossel aprofundado, não um parágrafo espremido num só.
- **Slide 1 é o teste de tudo**: nunca a definição do instituto jurídico
  ("O que é usucapião?") — abra com a situação, o número ou o
  mal-entendido que faz a pessoa parar de rolar o feed (ver
  `docs/perfil-escritorio.md`, "Gancho magnético"). Se o slide 1 poderia
  abrir qualquer post da mesma área, não é gancho — é preenchimento.

### Carrossel aprofundado
- **Extensão**: 7 slides.
- **Estrutura fixa**: gancho → contexto/identificação → o que a norma diz
  → primeiro desdobramento prático → segundo desdobramento (ou exceção) →
  comparação/exemplo genérico → encerramento sóbrio.
- **Entrega**: texto dos 7 slides + legenda.
- **Quando usar**: reservado a temas que genuinamente têm mais de uma
  camada — comparação de regimes, mudança legislativa com várias fases,
  instituto com múltiplas hipóteses. **Nunca usar só para "encher" um tema
  simples**: se o conteúdo dos slides 6-7 repete o que os slides 1-5 já
  disseram com outras palavras, o tema não pedia carrossel aprofundado —
  volte para o padrão de 5.

### Post estático
- **Extensão**: card único.
- **Estrutura fixa**: título → 2 a 3 linhas curtas de corpo → legenda.
- **Entrega**: texto do card + legenda.
- **O que a copy precisa entregar**: uma ideia só, dita do jeito mais curto
  que ainda fica claro — sem tentar caber o carrossel inteiro num card. Se
  o tema pede mais que 3 linhas de corpo, não é candidato a post estático
  naquela semana. O **título** carrega o gancho — é ele que decide se
  alguém para no card ou não; nunca o nome burocrático do instituto
  jurídico sozinho (ver `docs/perfil-escritorio.md`, "Gancho magnético").

### Reel rápido
- **Extensão**: roteiro de 12–15 segundos.
- **Estrutura fixa**: gancho (`0:00–0:03`) → um fato ou dica central
  (`0:03–0:12`) → fechamento com identificação (`0:12–0:15`) — sem
  desenvolvimento intermediário.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: a informação mais "compartilhável" do
  tema — um mito desfeito numa frase, uma dica isolada — nunca um resumo
  comprimido do Reel aprofundado. Se depois de cortar ainda sobra mais de
  uma ideia, o tema pede Reel aprofundado, não rápido.

### Reel aprofundado
- **Extensão**: roteiro de 30–45 segundos.
- **Estrutura fixa**: roteiro com marcação de tempo (ex.: `0:00–0:05`,
  `0:05–0:15`...) + texto que aparece na tela em cada trecho.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: gancho real nos primeiros 3 segundos
  — uma situação, número ou mal-entendido, nunca "hoje vamos falar sobre
  [instituto]" (ver `docs/perfil-escritorio.md`, "Gancho magnético") —,
  informação central até os 30s, fechamento sóbrio nos últimos segundos —
  sem CTA de conversão (Pergunta 04). Texto de tela curto: frases de até
  6-7 palavras, uma ideia por tela — não sub-título de artigo colado na
  tela.

## Legenda do Instagram — onde entra a profundidade técnica

Desde 2026-09-13, a legenda deixou de ser um resumo do card e passou a
carregar o que o card/reel não carrega: número de lei, artigo, nome e ano
de decisão, exceções e nuance. O card/reel existe para ser entendido em 3
segundos de rolagem; a legenda existe para quem parou e quer profundidade
— os dois têm função diferente, não são a mesma informação em dois
tamanhos.

- **Estrutura**: reforça a ideia central do card em 1-2 frases (sem
  repetir literalmente o texto do card) → aprofunda com a base legal
  específica (lei, artigo, decisão) e contexto/exceção relevante → fecha
  identificando a área de atuação do escritório (permitido pela Pergunta
  08 de `docs/normas-oab.md`).
- **Extensão**: sem o limite apertado do card — pode (e deve) ser mais
  densa —, mas ainda objetiva: sem redundância, sem frase de
  preenchimento (mesma régua de `docs/perfil-escritorio.md`, "Objetivo e
  enxuto").
- **Checklist OAB vale igual na legenda**: profundidade técnica não é
  isenção — nada de promessa de resultado (Regra 1), caso concreto (Regra
  2) ou urgência/alarmismo (Regra 5) só porque "é a legenda, não o card".

### Desvio editorial do rodízio de formato

O rodízio (ver "Instagram — rodízio de formato" abaixo) é a distribuição
padrão, mas não é obrigatório contra a evidência do próprio tema: se o
tema sorteado é claramente raso demais para 7 slides, ou denso demais para
caber em 15 segundos, troque para o formato que o tema pede. Registre a
troca e o motivo na seção "Pendências" de `calendario.md` — isso evita que
a exceção vire prática arbitrária e mantém o histórico auditável.

> **Descontinuado**: o formato Stories saiu do rodízio. Não usar em novas
> execuções.

## O formato do LinkedIn

### Texto longo
- **Extensão**: 180–300 palavras (reduzido de 250–400 em 2026-09-12 — o
  objetivo é objetividade, não menos profundidade: cortar redundância e
  frase de preenchimento, não cortar a análise em si).
- **Estrutura fixa**: nenhuma estrutura de slide — texto corrido, registro
  analítico, parágrafos completos.
- **Entrega**: texto completo pronto para publicação + eventual chamada de
  hashtags no fim (mais discretas que no Instagram).
- **O que a copy precisa entregar**: profundidade real dita da forma mais
  direta possível — é o formato onde cabe nuance, contexto histórico da
  norma, comparação antes/depois, mas cada frase precisa carregar
  informação nova. Não é o carrossel reescrito em prosa, e também não é
  redação floreada: corte a frase se ela só estiver preparando a próxima.
  **O primeiro parágrafo carrega o gancho**, nunca um parágrafo de
  contextualização genérica ("no cenário empresarial atual...") — abra
  direto com o risco, a mudança ou o número que interessa a quem decide
  na empresa (ver `docs/perfil-escritorio.md`, "Gancho magnético"); quem
  lê LinkedIn decide em uma linha se continua.
- Único formato do canal — os 3 posts semanais do LinkedIn usam sempre
  "Texto longo", sem rodízio.

### Registro: dois subtipos, proporção 80/20

Desde 2026-08-17, o LinkedIn existe para atrair empresas e reforçar o
escritório como referência técnica — não é o Instagram em texto mais longo.
Todo post continua passando pelo checklist de `docs/normas-oab.md` sem
exceção; o que muda é o **registro** da copy, em dois subtipos:

**Autoridade técnica (80% dos posts — 4 em cada 5)**
- Cita dispositivo legal com precisão (artigo, lei, decisão), não só "a lei
  diz que...".
- Compara antes/depois da norma, ou situa o tema num debate doutrinário ou
  jurisprudencial em curso — é o que demonstra domínio, não só informação.
- Framing de risco e gestão para quem decide na empresa: "o que sua empresa
  precisa observar", "o que muda na operação" — nunca "seus direitos como
  cidadão", que é o framing do Instagram.
- Mais denso e analítico — usa as 180–300 palavras para desenvolver
  argumento, não só listar fatos.

**Informativo direto (20% dos posts — 1 em cada 5)**
- Mesmo tom corporativo e mesma área/dia fixos, mas objetivo: "isto mudou,
  isto é o que significa na prática" — sem a camada extra de análise
  doutrinária. Serve para cobrir mais mudanças legislativas ao longo do
  tempo sem que todo post vire um ensaio.
- Ainda mais denso que o Instagram (é LinkedIn, público já é PJ), só não
  carrega a comparação/aprofundamento do subtipo acima.

**Como alternar**: a skill mantém um contador de posts de LinkedIn já
publicados (conta as linhas com `Canal = LinkedIn` em `temas/historico.md`).
A cada 5 posts consecutivos (posição `contador mod 5`), a posição `4`
(a cada 5ª) é **Informativo direto**; as posições `0`–`3` são **Autoridade
técnica**. Como o LinkedIn publica 3x/semana, o subtipo muda de área para
área dentro da mesma semana às vezes — não é "toda sexta é informativo",
é por post, na ordem cronológica de publicação.

**Em ambos os subtipos**: o fechamento pode nomear a área de atuação do
escritório relevante ao tema (permitido pela Pergunta 08 de
`docs/normas-oab.md`) — nunca com superlativo ("referência no mercado",
"líder") nem CTA de conversão (Pergunta 04). Autoridade se demonstra pela
precisão da análise, não por autoelogio.

## Instagram — rodízio de área (segunda, quarta e sexta)

**Desde 2026-09-12**, segunda, quarta e sexta deixaram de ter área fixa —
rotacionam entre as 5 áreas do escritório, para variar o que aparece em
cada dia da semana ao longo do tempo. Terça e quinta saem desse rodízio —
são sempre "Isenção de Imposto de Renda" (ver seção seguinte).

**Lista-base, ordem fixa**: `[Empresarial, Cível, Trabalhista, Tributário,
Previdenciário]` (índices 0 a 4).

**Como calcular a área de cada um dos 3 slots da semana**: calcule
`p = (3 × (N − 38)) mod 5`, onde `N` é o número da semana ISO alvo e `38`
é a âncora (2026-S38, primeira segunda-feira — 2026-09-14 — sob este
esquema). Os 3 posts da semana recebem, na ordem Segunda → Quarta → Sexta:
`LISTA[p]`, `LISTA[(p+1) mod 5]`, `LISTA[(p+2) mod 5]`.

Isso fecha um ciclo de 5 semanas (15 slots): cada uma das 5 áreas aparece
exatamente 3 vezes por ciclo, nunca duas vezes na mesma semana, e o dia da
semana em que cada área cai também varia de ciclo a ciclo — não existe
mais "toda segunda é Empresarial".

**Cível dentro do rodízio**: sempre que a área sorteada para um desses 3
slots for Cível, escolha o subtema entre os 5 arquivos de `temas/civel/`
pela mesma regra de anti-repetição (ver seção seguinte) — a rotação de
subtema é independente da rotação de área.

## Cível — subtemas (desde 2026-08-26)

Cível não tem mais um banco de temas único — o banco vive em
`temas/civel/`, um arquivo por subtema: `imobiliario.md`, `familia.md`,
`responsabilidade-civil.md`, `direito-das-coisas.md`, `contratos.md` (ver
`temas/civel/README.md`).

Cível não tem mais dia fixo — está sujeita ao mesmo rodízio de
segunda/quarta/sexta descrito acima. Sempre que a área sorteada para um
slot for Cível, escolha **qual subtema** usar aplicando a mesma regra de
anti-repetição de `temas/historico.md` nos 5 arquivos: pegue o primeiro
tema elegível (que não apareça no histórico), percorrendo os arquivos na
ordem listada acima, sem preferência fixa por subtema — a rotação entre
subtemas é consequência de qual banco ainda tem tema disponível, não uma
ordem pré-definida.

Registre o subtema escolhido no campo **Tema** do briefing (ex.: "Família
— União estável..."). No Notion, a propriedade `Área` continua sendo só
"Cível" — o Select não tem campo de subtema (ver `docs/notion.md`).

## Terça e quinta — Isenção de Imposto de Renda (desde 2026-09-12)

Terça e quinta do Instagram deixam de rotacionar área — toda semana, os
dois dias são sobre isenção de Imposto de Renda. No briefing e no Notion,
`Área` continua "Tributário" (é um recorte fixo dentro de Tributário, não
uma área nova no Select — ver `docs/notion.md`). O objetivo é dar peso
extra a um tema recorrente de alto interesse de busca sem esgotar o banco
geral de Tributário (`temas/tributario.md`), que continua servindo só o
slot de Tributário quando ele sai no rodízio de segunda/quarta/sexta.

**Banco próprio**: `temas/tributario-isencao-ir.md` — ângulos distintos de
isenção de IR (aposentadoria/doença grave, ganho de capital em imóvel
único, rendimentos de poupança, dependente com deficiência etc.). Mesma
regra de anti-repetição de `temas/historico.md` de qualquer outro banco:
cada ângulo só é usado uma vez até o banco se esgotar; como o assunto de
fundo é sempre o mesmo, escolher um ângulo ainda não publicado é o que
evita que os dois posts da semana (e as semanas entre si) pareçam
repetição do mesmo texto.

**Formato**: mesmo rodízio de 6 formatos dos outros posts do Instagram —
ver "Instagram — rodízio de formato" abaixo, trilha "Isenção de IR".

## Instagram — rodízio de formato

**Desde 2026-09-12**, formato deixou de ser amarrado a dia×área — sem área
fixa por dia, uma tabela de "semana do ciclo" por dia não faz mais
sentido. **Desde 2026-09-13**, o rodízio passou de 3 para 6 formatos (ver
"Os formatos do Instagram" acima). Formato roda por contagem, dentro de 6
"trilhas" independentes (as 5 áreas + o conteúdo fixo de Isenção de IR),
cada uma alternando sempre entre:

`[Carrossel curto, Carrossel padrão, Post estático, Reel rápido, Reel
aprofundado, Carrossel aprofundado]`

— sem repetir o mesmo formato duas vezes seguidas dentro da trilha:

- **Trilha de cada área** (Empresarial, Cível, Trabalhista, Previdenciário,
  e Tributário quando sai no rodízio de segunda/quarta/sexta): conte, em
  `temas/historico.md`, quantas linhas já têm `Canal = Instagram` e
  `Área = <a área>` — para Tributário, **exclua** as linhas cujo `Tema`
  começa com "Isenção de Imposto de Renda" (essas pertencem à trilha
  seguinte, não a esta). Esse número é o contador da trilha; o formato do
  novo post é a lista acima indexada por `contador mod 6`.
- **Trilha "Isenção de IR"** (terça e quinta): conte as linhas de
  `temas/historico.md` cujo `Tema` começa com "Isenção de Imposto de
  Renda" (`Área` sempre "Tributário" nessas linhas) — mesmo cálculo,
  `contador mod 6`. Dentro da mesma semana, calcule terça primeiro,
  incremente o contador em 1, calcule quinta em seguida — os dois nunca
  saem no mesmo formato na mesma semana.

**Desempate por colisão entre trilhas na mesma semana** (desde
2026-09-13): as 5-6 trilhas são independentes entre si, então nada impede
que duas trilhas diferentes cheguem ao **mesmo** índice na mesma semana —
descoberto num teste em que histórico simétrico (cada área com o mesmo
número de posts anteriores) fez 3 dos 5 posts da semana caírem no mesmo
formato. Para evitar isso: calcule o formato de cada um dos 5 posts do
Instagram **na ordem do calendário** (segunda → terça → quarta → quinta →
sexta). Se o formato calculado para um post já foi usado por outro post
**da mesma semana**, avance esse post para o próximo índice da lista (mod
6) que ainda não apareça nessa semana — repita o avanço se colidir de
novo. O primeiro post do calendário nunca é afetado por esta regra (não
há nada anterior na semana para colidir); os seguintes só avançam quando
há colisão real. Isso resolve por semana, sem guardar estado novo: o
formato que efetivamente sair (já resolvido o desempate) é o que conta
como incremento da trilha para a próxima vez que ela for sorteada — o
próprio `temas/historico.md`, de novo, é o único estado necessário.

Isso mantém a regra qualitativa de sempre variar formato dentro da mesma
trilha, sem exigir dia fixo nem ciclo de semana — o próprio histórico é o
estado, sem precisar guardar posição de ciclo em nenhum outro lugar. Ver
também "Desvio editorial do rodízio de formato" acima — o rodízio é a
distribuição padrão, não uma camisa de força contra a evidência do tema.

## LinkedIn — área × dia (fixo, sem rodízio)

Desde 2026-08-17, o LinkedIn é canal 100% B2B — só as 3 áreas inerentemente
corporativas, sempre as mesmas, sem alternância de grupo. Cível (incluindo
o subtema Família) e Previdenciário (áreas de pessoa física) saem do
LinkedIn e seguem só no Instagram.

| Dia | Área | Ângulo |
|---|---|---|
| Segunda | Empresarial | Societário, contratos, compliance, regulação de atividade econômica |
| Quarta | Trabalhista | Sempre pelo ângulo empregador/RH — obrigações, risco, gestão de pessoas. Mesmo que o tema em `temas/trabalhista.md` liste "Público: trabalhadores e RH", no LinkedIn o enquadramento é sempre pelo lado da empresa |
| Sexta | Tributário | Obrigações fiscais, planejamento lícito, reforma tributária |

Não há mais ciclo de semanas para o LinkedIn — essas 3 áreas se repetem
toda semana, sempre nesses dias. O que varia semana a semana é só o tema
escolhido (`temas/<area>.md`, sem repetir `temas/historico.md`) e o
subtipo de registro (Autoridade técnica × Informativo direto, proporção
80/20 — ver "Registro: dois subtipos" acima), nunca a área em si.

## Anti-repetição é por tema, não por canal

`temas/historico.md` é consultado e atualizado pelos dois calendários. Um
tema usado no Instagram não pode ser reusado no LinkedIn (nem vice-versa) —
a regra de não repetir tema (`CLAUDE.md`) vale para a automação inteira,
independente de canal.

**Repetição não é só título igual — é também ângulo parecido.** Antes de
fechar a escolha de um tema (passo 6 da skill), compare o **Ângulo
informativo** do candidato com os 2-3 temas mais recentes já publicados na
mesma área/trilha (`temas/historico.md` + o próprio banco). Se dois temas
tratam essencialmente do mesmo recorte com palavras diferentes, prefira o
próximo elegível do banco, mesmo que o título não seja idêntico — títulos
distintos com o mesmo ângulo são a forma mais comum de repetição
disfarçada, e é isso que faz a semana parecer "mais do mesmo" mesmo sem
violar a regra literal de não repetir tema. Bancos muito curtos (poucos
temas cadastrados) são a causa mais comum desse problema — sinalize no
briefing (seção "Pendências") quando um banco estiver perto de esgotar,
para curadoria futura.
