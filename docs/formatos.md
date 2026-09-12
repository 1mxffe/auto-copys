# Canais, formatos e rodízio

## Canais e cadência

O escritório mantém **dois calendários editoriais separados**, cada um com
cadência própria — não é mais um único calendário de 6 posts:

| Canal | Posts/semana | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" (sem rodízio) |
| Instagram | 5 | Segunda, terça, quarta, quinta e sexta (sem sábado) | Rodízio entre Carrossel, Post estático e Reel |

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

## Os 3 formatos do Instagram

### Carrossel
- **Extensão**: 5 slides.
- **Estrutura fixa**: capa/gancho → identificação (o que é / por que
  importa) → informação-chave → aprofundamento → encerramento sóbrio.
- **Entrega**: texto de cada um dos 5 slides + legenda de publicação.
- **O que a copy precisa entregar**: cada slide deve fazer sentido lido
  isoladamente (usuário desliza rápido), mas a sequência tem que fechar uma
  ideia completa até o slide 5. Curto por slide: até ~25 palavras além do
  gancho/título — se um slide precisa de mais que isso, é sinal de que o
  tema pede dois slides, não um parágrafo espremido num só.

### Post estático
- **Extensão**: card único.
- **Estrutura fixa**: título → 2 a 3 linhas curtas de corpo → legenda.
- **Entrega**: texto do card + legenda.
- **O que a copy precisa entregar**: uma ideia só, dita do jeito mais curto
  que ainda fica claro — sem tentar caber o carrossel inteiro num card. Se
  o tema pede mais que 3 linhas de corpo, não é candidato a post estático
  naquela semana.

### Reel / vídeo curto
- **Extensão**: roteiro de 30–45 segundos.
- **Estrutura fixa**: roteiro com marcação de tempo (ex.: `0:00–0:05`,
  `0:05–0:15`...) + texto que aparece na tela em cada trecho.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: gancho nos primeiros 3 segundos,
  informação central até os 30s, fechamento sóbrio nos últimos segundos —
  sem CTA de conversão (Pergunta 04). Texto de tela curto: frases de até
  6-7 palavras, uma ideia por tela — não sub-título de artigo colado na
  tela.

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

**Formato**: mesmo rodízio de Carrossel / Post estático / Reel dos outros
posts do Instagram — ver "Instagram — rodízio de formato" abaixo, trilha
"Isenção de IR".

## Instagram — rodízio de formato

**Desde 2026-09-12**, formato deixou de ser amarrado a dia×área — sem área
fixa por dia, uma tabela de "semana do ciclo" por dia não faz mais
sentido. Formato agora roda por contagem, dentro de 6 "trilhas"
independentes (as 5 áreas + o conteúdo fixo de Isenção de IR), cada uma
alternando sempre entre `[Carrossel, Post estático, Reel]` sem repetir a
mesma trilha duas vezes seguidas:

- **Trilha de cada área** (Empresarial, Cível, Trabalhista, Previdenciário,
  e Tributário quando sai no rodízio de segunda/quarta/sexta): conte, em
  `temas/historico.md`, quantas linhas já têm `Canal = Instagram` e
  `Área = <a área>` — para Tributário, **exclua** as linhas cujo `Tema`
  começa com "Isenção de Imposto de Renda" (essas pertencem à trilha
  seguinte, não a esta). Esse número é o contador da trilha; o formato do
  novo post é `[Carrossel, Post estático, Reel][contador mod 3]`.
- **Trilha "Isenção de IR"** (terça e quinta): conte as linhas de
  `temas/historico.md` cujo `Tema` começa com "Isenção de Imposto de
  Renda" (`Área` sempre "Tributário" nessas linhas) — mesmo cálculo,
  `contador mod 3`. Dentro da mesma semana, calcule terça primeiro,
  incremente o contador em 1, calcule quinta em seguida — os dois nunca
  saem no mesmo formato na mesma semana.

Isso mantém a regra qualitativa de sempre variar formato dentro da mesma
trilha, sem exigir dia fixo nem ciclo de semana — o próprio histórico é o
estado, sem precisar guardar posição de ciclo em nenhum outro lugar.

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
