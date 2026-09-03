# Canais, formatos e rodízio

## Canais e cadência

O escritório mantém **dois calendários editoriais separados**, cada um com
cadência própria — não é mais um único calendário de 6 posts:

| Canal | Posts/semana | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" (sem rodízio) |
| Instagram | 4 | Segunda, quarta, quinta e sexta (sem post na terça nem no sábado) | Rodízio entre Carrossel, Post estático e Reel, por post |

Desde 2026-08-26 o Instagram não publicava às sextas-feiras — Família
deixou de ser área própria do calendário e virou subtema de Cível (ver
"Cível — subtemas" abaixo).

**Desde 2026-09-03**, nova reorganização, decisão editorial explícita do
usuário: o Instagram passou de 5 para 4 posts semanais e trocou terça e
sábado por sexta — os dias passaram a ser Segunda, Quarta, Quinta e Sexta.
Segunda, quarta e sexta continuam cobrindo as áreas gerais do escritório,
mas agora em **rodízio semanal** entre elas (ver "Instagram — área × dia"
abaixo) em vez de dia fixo por área. Quinta-feira passa a ser **exclusiva**
da categoria de produto "Isenção de Imposto de Renda" (aposentados,
pensionistas e portadores de doença grave — Lei 7.713/88), com banco
próprio em `temas/isencao-ir.md` — não é uma área do direito, não entra no
rodízio de área, não é substituída em nenhuma semana. Previdenciário deixou
de ter espaço no calendário do Instagram (opção mantida como legado no
Select "Área" do Notion — ver `docs/notion.md` — sem novas atribuições). O
volume total da semana passou de 8 para 7 posts.

"Site institucional" segue listado como canal da marca em
`docs/perfil-escritorio.md`, mas não tem formato nem calendário definidos
nesta automação — fora de escopo até ser desenhado à parte.

Cada canal gera sua própria pasta de saída dentro da mesma semana:
`calendarios/AAAA-SNN/linkedin/` e `calendarios/AAAA-SNN/instagram/` (ver
`.claude/skills/calendario-semanal/SKILL.md`).

## Os 3 formatos do Instagram

### Carrossel
- **Extensão**: 2 a 5 slides (cards) — desde 2026-09-03 deixou de ser
  extensão fixa de 5; o número de slides varia conforme o quanto o tema
  comporta.
- **Estrutura fixa**: capa/gancho → identificação (o que é / por que
  importa) → informação-chave → [aprofundamento, se houver slides
  suficientes] → encerramento sóbrio. Com 2 slides, vá direto de
  capa/gancho para um encerramento que já entrega a informação-chave; com
  5, use a sequência completa.
- **Entrega**: texto de cada slide (2 a 5) + legenda de publicação.
- **O que a copy precisa entregar**: cada slide deve fazer sentido lido
  isoladamente (usuário desliza rápido), mas a sequência tem que fechar uma
  ideia completa até o último slide, qualquer que seja a extensão da
  semana.

### Post estático
- **Extensão**: card único.
- **Estrutura fixa**: título → 3 a 4 linhas de corpo → legenda.
- **Entrega**: texto do card + legenda.
- **O que a copy precisa entregar**: uma ideia só, sem tentar caber o
  carrossel inteiro num card — se o tema pede mais que 4 linhas de corpo,
  não é candidato a post estático naquela semana.

### Reel / vídeo curto
- **Extensão**: roteiro de 30–45 segundos.
- **Estrutura fixa**: roteiro com marcação de tempo (ex.: `0:00–0:05`,
  `0:05–0:15`...) + texto que aparece na tela em cada trecho.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: gancho nos primeiros 3 segundos,
  informação central até os 30s, fechamento sóbrio nos últimos segundos —
  sem CTA de conversão (Pergunta 04).

> **Descontinuado**: o formato Stories saiu do rodízio. Não usar em novas
> execuções.

## O formato do LinkedIn

### Texto longo
- **Extensão**: 250–400 palavras.
- **Estrutura fixa**: nenhuma estrutura de slide — texto corrido, registro
  analítico, parágrafos completos.
- **Entrega**: texto completo pronto para publicação + eventual chamada de
  hashtags no fim (mais discretas que no Instagram).
- **O que a copy precisa entregar**: profundidade real — é o formato onde
  cabe nuance, contexto histórico da norma, comparação antes/depois. Não é
  o carrossel reescrito em prosa.
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

**Em ambos os subtipos**: o fechamento pode nomear a área de atuação do
escritório relevante ao tema (permitido pela Pergunta 08 de
`docs/normas-oab.md`) — nunca com superlativo ("referência no mercado",
"líder") nem CTA de conversão (Pergunta 04). Autoridade se demonstra pela
precisão da análise, não por autoelogio.

## Instagram — área × dia (desde 2026-09-03)

Segunda, quarta e sexta rotacionam entre as 4 áreas gerais — Empresarial,
Cível, Trabalhista, Tributário —, num ciclo de 4 semanas: a cada semana,
exatamente uma área fica de fora, e as outras três ocupam Segunda, Quarta
e Sexta, num rodízio que também troca qual área cai em qual dia (nenhuma
área fica presa a um dia fixo). Quinta-feira **não** entra nesse rodízio —
é fixa, sempre "Isenção de IR" (ver seção própria abaixo).

| Posição do ciclo | Segunda | Quarta | Sexta | (fora nesta semana) |
|---|---|---|---|---|
| 0 | Empresarial | Cível | Trabalhista | Tributário |
| 1 | Tributário | Empresarial | Cível | Trabalhista |
| 2 | Trabalhista | Tributário | Empresarial | Cível |
| 3 | Cível | Trabalhista | Tributário | Empresarial |

O ciclo reinicia na posição 4 (= posição 0 novamente). Para saber em que
posição do ciclo uma execução está, use `(N - 37) mod 4` — `N` é o número
da semana ISO alvo; `37` é a primeira semana gerada já sob este esquema
(o esquema anterior, de dia fixo por área, valeu até a semana 2026-S36
inclusive — a reorganização foi decidida em 2026-09-03, no meio da
2026-S36 já em andamento, e não é retroativa a essa semana).

Cada área, ao longo do ciclo de 4 semanas, passa 3 semanas no calendário e
1 semana de fora — nenhuma fica ausente por muito tempo, e não há
preferência fixa entre elas além do que a tabela acima determina.

## Cível — subtemas (desde 2026-08-26)

Cível não tem mais um banco de temas único — o banco vive em
`temas/civel/`, um arquivo por subtema: `imobiliario.md`, `familia.md`,
`responsabilidade-civil.md`, `direito-das-coisas.md`, `contratos.md` (ver
`temas/civel/README.md`).

Desde 2026-09-03, Cível não tem mais um dia fixo — cai em Segunda, Quarta
ou Sexta conforme a posição do ciclo de área da semana (ver acima). Em
qualquer dia que Cível apareça numa semana, para escolher **qual subtema**
usar, aplique a mesma regra de anti-repetição de `temas/historico.md` nos
5 arquivos: pegue o primeiro tema elegível (que não apareça no histórico),
percorrendo os arquivos na ordem listada acima, sem preferência fixa por
subtema — a rotação entre subtemas é consequência de qual banco ainda tem
tema disponível, não uma ordem pré-definida.

Registre o subtema escolhido no campo **Tema** do briefing (ex.: "Família
— União estável..."). No Notion, a propriedade `Área` continua sendo só
"Cível" — o Select não tem campo de subtema (ver `docs/notion.md`).

## Instagram — quinta-feira: "Isenção de IR" (desde 2026-09-03)

Quinta-feira é fixa, toda semana, para a categoria de produto **"Isenção
de Imposto de Renda"** — aposentados, pensionistas e portadores de doença
grave, Lei 7.713/88. Não é uma área do direito (por isso não entra no
rodízio de área acima) e não é substituída por nenhuma outra pauta: se o
banco ficar sem tema elegível, é sinal de que `temas/isencao-ir.md`
precisa de reforço editorial, não motivo para pular a semana.

- **Banco de temas**: `temas/isencao-ir.md` — mesma regra de
  anti-repetição de `temas/historico.md` que as demais áreas.
- **Tom e compliance específicos**: leia `docs/produto-isencao-ir.md`
  antes de escrever qualquer post desta pauta — tem a análise da
  referência de mercado (VSH Isenta) e um reforço de compliance que soma
  ao checklist geral de `docs/normas-oab.md`, não o substitui.
- **Área no Notion**: opção própria `"Isenção de IR"` no Select "Área" (ver
  `docs/notion.md`) — não usar "Previdenciário" nem "Tributário", ainda que
  o tema tenha proximidade com os dois.
- **Formato**: participa do mesmo contador global de formato dos outros 3
  posts de Instagram da semana (ver seção seguinte) — não tem formato
  fixo próprio.

## Instagram — rodízio de formato (contador global, por post)

Desde 2026-09-03, o rodízio de formato deixou de ser uma matriz fixa por
área×dia — como a área não tem mais dia fixo (seção acima), o formato
passa a ser um **contador global por post**, no mesmo padrão do rodízio de
registro do LinkedIn (ver "Registro: dois subtipos" acima).

A skill mantém um contador de posts de Instagram já publicados (conta as
linhas com `Canal = Instagram` em `temas/historico.md`). Para cada novo
post de Instagram da semana, na ordem cronológica de publicação (Segunda →
Quarta → Quinta → Sexta), incremente o contador e calcule `contador mod
3`:

| contador mod 3 | Formato |
|---|---|
| 0 | Reel |
| 1 | Post estático |
| 2 | Carrossel |

O post de "Isenção de IR" da quinta-feira participa do mesmo contador que
os posts de Segunda, Quarta e Sexta — não tem sequência própria.

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

## Os ciclos do Instagram e do LinkedIn são independentes

O Instagram tem, desde 2026-09-03, dois mecanismos próprios e
independentes entre si: o ciclo de área de 4 semanas para Segunda/Quarta/
Sexta, e o contador global de formato por post (ambos acima) — mais a
quinta-feira fixa de "Isenção de IR", que não participa do ciclo de área.
O LinkedIn não tem ciclo de semana — as 3 áreas são fixas todo período, e o
que varia é o contador de registro (Autoridade técnica × Informativo
direto). Não há combinação de ciclos entre canais.

## Anti-repetição é por tema, não por canal

`temas/historico.md` é consultado e atualizado pelos dois calendários. Um
tema usado no Instagram não pode ser reusado no LinkedIn (nem vice-versa) —
a regra de não repetir tema (`CLAUDE.md`) vale para a automação inteira,
independente de canal.
