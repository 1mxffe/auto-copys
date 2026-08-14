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
- **Estrutura fixa**: capa/gancho → identificação (o que é / por que
  importa) → informação-chave → aprofundamento → encerramento sóbrio.
- **Entrega**: texto de cada um dos 5 slides + legenda de publicação.
- **O que a copy precisa entregar**: cada slide deve fazer sentido lido
  isoladamente (usuário desliza rápido), mas a sequência tem que fechar uma
  ideia completa até o slide 5.

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
> execuções — as únicas peças em Stories que existem são as da semana
> 2026-S34 (ensaio manual, esquema antigo), preservadas como estão.

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
semana do ciclo do Instagram uma execução está, use `((N - 35) mod 3) + 1`
— `N` é o número da semana ISO e `35` é a primeira semana gerada já sob
este esquema (a semana 34 foi o ensaio manual, sob o esquema antigo de
5 formatos e 1 calendário só, e não entra nesta conta).

## LinkedIn — área × dia (grupo alternado, ciclo de 2 semanas)

Só 3 áreas por semana cabem no LinkedIn. As 6 áreas se revezam em dois
grupos de 3, alternando semana sim, semana não — toda área aparece no
LinkedIn a cada 2 semanas:

**Grupo 1 (semana ímpar do ciclo)**

| Dia | Área |
|---|---|
| Segunda | Empresarial |
| Quarta | Trabalhista |
| Sexta | Família |

**Grupo 2 (semana par do ciclo)**

| Dia | Área |
|---|---|
| Segunda | Cível |
| Quarta | Tributário |
| Sexta | Previdenciário |

Use `(N - 35) mod 2`: resto `0` → Grupo 1, resto `1` → Grupo 2.

## Combinando os dois ciclos

O ciclo do Instagram (3 semanas) e o do LinkedIn (2 semanas) têm mínimo
múltiplo comum de 6 — o panorama completo (quem publica o quê, em qual
formato, nos dois canais) se repete a cada 6 semanas.

## Anti-repetição é por tema, não por canal

`temas/historico.md` é consultado e atualizado pelos dois calendários. Um
tema usado no Instagram não pode ser reusado no LinkedIn (nem vice-versa) —
a regra de não repetir tema (`CLAUDE.md`) vale para a automação inteira,
independente de canal.
