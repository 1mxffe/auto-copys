# Canais, formatos e rodízio

## Canais e cadência

O escritório mantém **dois calendários editoriais separados**, cada um com
cadência própria — não é mais um único calendário de 6 posts:

| Canal | Posts/semana | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" (legenda) + visual obrigatório (Carrossel curto ou Card estático, conforme o subtipo — sem rodízio independente) |
| Instagram | 6 | Segunda a sábado | Rodízio entre Carrossel, Post estático e Reel |

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
  ideia completa até o slide 5.
- **Copy enxuta**: uma ideia por slide, frase curta, sem parágrafo denso.
  Tetos de tamanho e instrução de título/subtítulo/ícone/imagem por slide
  em `templates/briefing-post.md`, seções 4 e 6.

### Post estático
- **Extensão**: card único.
- **Estrutura fixa**: título → 3 a 4 linhas de corpo → legenda.
- **Entrega**: texto do card + legenda.
- **O que a copy precisa entregar**: uma ideia só, sem tentar caber o
  carrossel inteiro num card — se o tema pede mais que 4 linhas de corpo,
  não é candidato a post estático naquela semana.
- **Copy enxuta**: se o corpo lista mais de um item (ex.: "3 cláusulas",
  "2 prazos"), usar marcadores — nunca emendar os itens numa frase corrida
  só para caber em "4 linhas". Tetos de tamanho e instrução de
  título/subtítulo/ícone/imagem em `templates/briefing-post.md`, seções 4
  e 6.

### Reel / vídeo curto
- **Extensão**: roteiro de 30–45 segundos.
- **Estrutura fixa**: roteiro com marcação de tempo (ex.: `0:00–0:05`,
  `0:05–0:15`...) + texto que aparece na tela em cada trecho.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: gancho nos primeiros 3 segundos,
  informação central até os 30s, fechamento sóbrio nos últimos segundos —
  sem CTA de conversão (Pergunta 04).
- **Copy enxuta**: texto de tela ≤ 10 palavras por trecho de tempo — a
  fala pode detalhar um pouco mais, mas sem sair da ideia daquele trecho.
  Tetos completos e instrução de título/subtítulo/ícone/imagem por tela em
  `templates/briefing-post.md`, seções 4 e 6.

> **Descontinuado**: o formato Stories saiu do rodízio. Não usar em novas
> execuções.

## O formato do LinkedIn

Desde 2026-08-19, todo post do LinkedIn tem **dois componentes obrigatórios**,
sempre juntos — nunca um sem o outro:

1. **Texto longo** (a legenda/corpo do post) — a análise, o que sustenta
   "autoridade técnica".
2. **Visual** (Carrossel curto ou Card estático) — o que aparece no feed
   antes de qualquer clique em "ver mais". Só texto não segura a atenção;
   o visual é o gancho.

### Texto longo (legenda)
- **Extensão**: 250–400 palavras.
- **Estrutura fixa**: nenhuma estrutura de slide — texto corrido, registro
  analítico, parágrafos completos.
- **Entrega**: texto completo pronto para publicação + eventual chamada de
  hashtags no fim (mais discretas que no Instagram).
- **O que a copy precisa entregar**: profundidade real — é o formato onde
  cabe nuance, contexto histórico da norma, comparação antes/depois. Não é
  o carrossel reescrito em prosa.
- Único formato de texto do canal — os 3 posts semanais do LinkedIn usam
  sempre "Texto longo" como legenda, sem rodízio. O rodízio do canal está
  no visual que acompanha (ver abaixo), não no texto.

### Visual obrigatório: Carrossel curto ou Card estático

O visual **não duplica** o texto longo — é um resumo/gancho autônomo, que
faz sentido mesmo para quem não vai clicar em "ver mais". Qual dos dois
formatos usar é determinado pelo subtipo de registro do post (ver abaixo),
não por escolha livre a cada semana.

**Carrossel curto** (post em registro Autoridade técnica)
- **Extensão**: até 5 cards (pode ser menos — 3 ou 4 — se o argumento
  fechar antes; nunca mais que 5, é "curto" por definição).
- **Estrutura**: capa (a tese do post, curta) → 1–3 cards de
  desenvolvimento (dado, comparação antes/depois, dispositivo legal) →
  encerramento + identificação do escritório.
- **Registro visual**: sóbrio e corporativo — sem o tom didático-leigo do
  carrossel do Instagram; cada card já pressupõe público PJ.
- **O que a copy precisa entregar**: a versão "manchete" dos pontos que o
  texto longo desenvolve — não repete frase do texto, resume a ideia em
  poucas palavras. Tetos de tamanho em `templates/briefing-post.md`, seção
  4 (mesmo teto do Carrossel do Instagram, ≤ 25 palavras por card).

**Card estático** (post em registro Informativo direto)
- **Extensão**: 1 card único.
- **Estrutura**: título (a mudança/fato) + subtítulo curto (o que significa
  na prática).
- **O que a copy precisa entregar**: uma informação só, objetiva — o
  mesmo espírito objetivo do subtipo Informativo direto, em forma de
  card. Tetos de tamanho em `templates/briefing-post.md`, seção 4 (mesmo
  teto do Post estático do Instagram).

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
- Mais denso e analítico — usa as 250–400 palavras para desenvolver
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

**O mesmo cálculo decide o visual** — não há contador separado:
`contador mod 5` = `4` → Informativo direto → **Card estático**;
`contador mod 5` = `0`–`3` → Autoridade técnica → **Carrossel curto**.

**Em ambos os subtipos**: o fechamento (no texto e no visual) pode nomear a
área de atuação do escritório relevante ao tema (permitido pela Pergunta 08
de `docs/normas-oab.md`) — nunca com superlativo ("referência no mercado",
"líder") nem CTA de conversão (Pergunta 04). Autoridade se demonstra pela
precisão da análise, não por autoelogio — no texto ou no card.

## Instagram — área × dia (fixo)

Cada área tem um dia fixo, toda semana:

| Dia | Área |
|---|---|
| Segunda | Empresarial |
| Terça | Cível |
| Quarta | Trabalhista |
| Quinta | Tributário |
| Sexta | Família |
| Sábado | Previdenciário |

## Instagram — rodízio de formato (ciclo de 3 semanas)

Formato por dia, variando por semana do ciclo — cada área passa pelos 3
formatos ao longo de 3 semanas, sem repetir o mesmo formato em duas semanas
seguidas na mesma área:

**Semana 1 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Carrossel |
| Terça | Cível | Post estático |
| Quarta | Trabalhista | Reel |
| Quinta | Tributário | Carrossel |
| Sexta | Família | Post estático |
| Sábado | Previdenciário | Reel |

**Semana 2 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Post estático |
| Terça | Cível | Reel |
| Quarta | Trabalhista | Carrossel |
| Quinta | Tributário | Post estático |
| Sexta | Família | Reel |
| Sábado | Previdenciário | Carrossel |

**Semana 3 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Reel |
| Terça | Cível | Carrossel |
| Quarta | Trabalhista | Post estático |
| Quinta | Tributário | Reel |
| Sexta | Família | Carrossel |
| Sábado | Previdenciário | Post estático |

O ciclo reinicia na semana 4 (= semana 1 novamente). Para saber em que
semana do ciclo do Instagram uma execução está, use `((N - 34) mod 3) + 1`
— `N` é o número da semana ISO e `34` é a primeira semana gerada já sob
este esquema (a semana 2026-S34 foi regenerada em 2026-08-14 para
substituir o ensaio antigo de 5 formatos e 1 calendário só).

## LinkedIn — área × dia (fixo, sem rodízio)

Desde 2026-08-17, o LinkedIn é canal 100% B2B — só as 3 áreas inerentemente
corporativas, sempre as mesmas, sem alternância de grupo. Cível, Família e
Previdenciário (áreas de pessoa física) saem do LinkedIn e seguem só no
Instagram.

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

## O ciclo do Instagram continua sozinho

Sem o ciclo do LinkedIn, só resta o ciclo de 3 semanas do Instagram (ver
seção acima) — não há mais combinação de ciclos entre canais.

## Anti-repetição é por tema, não por canal

`temas/historico.md` é consultado e atualizado pelos dois calendários. Um
tema usado no Instagram não pode ser reusado no LinkedIn (nem vice-versa) —
a regra de não repetir tema (`CLAUDE.md`) vale para a automação inteira,
independente de canal.
