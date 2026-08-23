# Canais, formatos e rodízio

## Canais e cadência

O escritório mantém **dois calendários editoriais separados**, cada um com
cadência própria — não é mais um único calendário de 6 posts:

| Canal | Posts/semana | Dias | Formato |
|---|---|---|---|
| LinkedIn | 3 | Segunda, quarta, sexta | Sempre "Texto longo" (sem rodízio) |
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
- **Estrutura padrão**: capa/gancho → identificação (o que é / por que
  importa) → informação-chave → aprofundamento → encerramento sóbrio. Pode
  ser substituída por uma das estruturas de conteúdo abaixo ("Instagram —
  estruturas de conteúdo"), mantendo os 5 slides.
- **Entrega**: texto de cada um dos 5 slides + legenda de publicação.
- **O que a copy precisa entregar**: cada slide deve fazer sentido lido
  isoladamente (usuário desliza rápido), mas a sequência tem que fechar uma
  ideia completa até o slide 5.

### Post estático
- **Extensão**: card único.
- **Estrutura padrão**: título → 3 a 4 linhas de corpo → legenda. Pode ser
  substituída por uma das estruturas de conteúdo abaixo compatíveis com
  card único.
- **Entrega**: texto do card + legenda.
- **O que a copy precisa entregar**: uma ideia só, sem tentar caber o
  carrossel inteiro num card — se o tema pede mais que 4 linhas de corpo,
  não é candidato a post estático naquela semana.

### Reel / vídeo curto
- **Extensão**: roteiro de 30–45 segundos.
- **Estrutura padrão**: roteiro com marcação de tempo (ex.: `0:00–0:05`,
  `0:05–0:15`...) + texto que aparece na tela em cada trecho. Pode ser
  substituída por uma das estruturas de conteúdo abaixo compatíveis com
  roteiro curto.
- **Entrega**: roteiro marcado + texto de tela + legenda.
- **O que a copy precisa entregar**: gancho nos primeiros 3 segundos,
  informação central até os 30s, fechamento sóbrio nos últimos segundos —
  sem CTA de conversão (Pergunta 04).

> **Descontinuado**: o formato Stories saiu do rodízio. Não usar em novas
> execuções.

## Instagram — estruturas de conteúdo (banco de testes)

Desde 2026-08-20, cada um dos 6 posts de Instagram, além do formato visual
(Carrossel/Post estático/Reel — inalterado), recebe também uma **estrutura
de conteúdo**: a arquitetura interna da peça (o que vem em cada slide/tela,
em que ordem). O objetivo é deliberadamente testar variedade — algumas
estruturas vão performar melhor que outras, e é isso que o relatório de
métricas (`templates/relatorio-semanal.md`, seção "Desempenho por
estrutura de conteúdo") mede ao longo do tempo, alimentando
`docs/aprendizados.md`.

Isso nasceu de uma varredura de perfis de outros escritórios de advocacia
no Instagram (2026-08-20) — ver o raciocínio completo no histórico da
sessão que criou esta seção. Um padrão problemático identificado nessa
varredura (narrativa de caso real, mesmo anonimizada, com desfecho de
processo) foi deliberadamente **excluído** da lista abaixo — ver nota na
estrutura "Situação".

### As 8 estruturas (7 alternativas + o padrão)

**Padrão** (a estrutura original, ver descrição de cada formato acima) —
capa/gancho → identificação → informação-chave → aprofundamento →
encerramento. Compatível com Carrossel, Post estático, Reel.

**Situação** — protagonista genérico, sem nome e **sem caso real** (é uma
situação ilustrativa, não um processo específico) → o que a lei diz sobre
essa situação → fechamento com o que fazer. **Atenção de conformidade**:
nunca narrar um desfecho de processo ("a Justiça reconheceu...", "o
benefício foi concedido..."), mesmo com protagonista anônimo — isso soa
como caso concreto patrocinado pelo escritório, vedado pela Regra 2 /
Pergunta 06 de `docs/normas-oab.md`. Fechar na tensão informativa ("é isso
que a lei garante nessa situação"), nunca no resultado de uma ação.
Compatível com Carrossel, Reel.

**Mito x verdade** — mito popular ou crença comum e errada (capa) → o que
a lei realmente diz → por que o mito persiste ou qual a consequência
prática de acreditar nele. Compatível com Carrossel, Post estático.

**Checklist / lista rápida** — N itens práticos e objetivos, um por slide
(ex.: "5 documentos que você precisa guardar para X"). Em Post estático,
versão condensada (3-4 itens em texto corrido, não um por linha). Alto
potencial de salvamento — é o tipo de conteúdo que a pessoa guarda pra
consultar depois, não só curte. Compatível com Carrossel, Post estático.

**Antes x depois da norma** — regra antiga → o que mudou (lei, reforma,
decisão) → regra nova e o que muda na prática. Já existe como parte do
registro "Autoridade técnica" do LinkedIn (`docs/formatos.md`, seção
"Registro: dois subtipos") — aqui é a versão Instagram, mais direta e sem
a camada de análise doutrinária. Compatível com Carrossel, Post estático,
Reel.

**Pergunta frequente** — uma pergunta genérica e recorrente (nunca a
pergunta literal de um seguidor específico, o que a tornaria identificável
e beiraria "caso concreto") → resposta direta e objetiva. Pode simular a
estética de "pergunta recebida" (ex.: caixa de pergunta no design) desde
que a pergunta em si seja formulada como uma dúvida comum, não a
transcrição de uma mensagem real. Compatível com Reel (tom mais
conversacional), Carrossel.

**Glossário** — um termo jurídico técnico, explicado em linguagem simples,
com um exemplo neutro (não um caso real). Ajuda o público leigo do
Instagram a se situar antes de ler outros posts da área. Compatível com
Post estático.

**Atualização de tema** — revisita um tema já publicado (consultar
`temas/historico.md`) que teve uma mudança legislativa ou jurisprudencial
nova desde a publicação original ("Atualização: o que mudou desde que
falamos sobre X") — não é repetição de tema, é continuidade editorial
sobre o mesmo assunto. Ainda passa pela checagem normal de anti-repetição
de `temas/historico.md` para o tema em si; o que muda é o ângulo
(atualização, não o tema original de novo). Compatível com Carrossel,
Post estático, Reel.

### Como a estrutura é escolhida a cada post

Ver `.claude/skills/calendario-semanal/SKILL.md`, passo 5 — a skill escolhe,
entre as estruturas compatíveis com o formato do dia, a que apareceu há
mais tempo (ou nunca) na coluna "Estrutura" de `temas/historico.md`. Isso
garante rotação real ao longo das semanas em vez de a mesma estrutura se
tornar o novo padrão engessado — o ponto é gerar dado suficiente pra
`docs/aprendizados.md` eventualmente indicar quais estruturas performam
melhor por área/formato.

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
