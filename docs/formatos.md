# Formatos e rodízio

## Os 5 formatos

### Carrossel (Instagram/LinkedIn)
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

### Stories
- **Extensão**: 3 telas encadeadas.
- **Estrutura fixa**: 3 telas + 1 elemento interativo (enquete ou caixinha
  informativa — nunca caixinha de pergunta jurídica aberta a caso concreto,
  ver Pergunta 01 em `docs/normas-oab.md`).
- **Entrega**: texto das 3 telas + a enquete/caixinha proposta.
- **O que a copy precisa entregar**: a informação já útil na tela 1 (quem só
  vê a primeira tela ainda sai com algo); telas 2–3 aprofundam.

### LinkedIn (texto longo)
- **Extensão**: 250–400 palavras.
- **Estrutura fixa**: nenhuma estrutura de slide — texto corrido, registro
  analítico, parágrafos completos.
- **Entrega**: texto completo pronto para publicação + eventual chamada de
  hashtags no fim (mais discretas que no Instagram).
- **O que a copy precisa entregar**: profundidade real — é o formato onde
  cabe nuance, contexto histórico da norma, comparação antes/depois. Não é
  o carrossel reescrito em prosa.

## Matriz de rodízio (ciclo de 3 semanas)

Cada área passa por um formato diferente a cada semana, num ciclo de 3
semanas, para o feed não repetir o mesmo par área×formato toda semana.

**Semana 1 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Carrossel |
| Terça | Cível | Post estático |
| Quarta | Trabalhista | Reel |
| Quinta | Tributário | Carrossel |
| Sexta | Família | Stories |
| Sábado | Previdenciário | LinkedIn |

**Semana 2 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Stories |
| Terça | Cível | Carrossel |
| Quarta | Trabalhista | Post estático |
| Quinta | Tributário | Reel |
| Sexta | Família | Carrossel |
| Sábado | Previdenciário | Post estático |

**Semana 3 do ciclo**

| Dia | Área | Formato |
|---|---|---|
| Segunda | Empresarial | Post estático |
| Terça | Cível | Reel |
| Quarta | Trabalhista | Carrossel |
| Quinta | Tributário | Stories |
| Sexta | Família | LinkedIn |
| Sábado | Previdenciário | Carrossel |

O ciclo reinicia na semana 4 (= semana 1 novamente). Para saber em que
semana do ciclo uma execução está, conte a partir da primeira semana gerada
pela automação (Semana 34/2026 = semana 1 do ciclo) e aplique
`((N - 34) mod 3) + 1`.

Formato LinkedIn é sempre reservado a uma área por semana (evita saturar o
canal); Carrossel pode se repetir entre áreas na mesma semana, já que sai em
dias e contas diferentes.
