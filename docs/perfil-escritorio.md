# Perfil do escritório — Gutmann & Silva

Referência de marca e tom de voz para toda peça gerada pela automação. Serve
para manter consistência entre os 8 posts semanais dos dois calendários
(LinkedIn e Instagram — ver `docs/formatos.md`), mesmo escritos em sessões
diferentes, meses de distância.

## Identidade

- **Nome**: Gutmann & Silva Advogados Associados
- **Áreas de atuação cobertas pelo calendário**: Direito Empresarial,
  Direito Cível (com os subtemas Imobiliário, Família, Responsabilidade
  Civil, Direito das Coisas e Contratos), Direito Trabalhista, Direito
  Tributário, Direito Previdenciário.
- **Canais**: Instagram e LinkedIn têm calendário editorial próprio nesta
  automação — cadência, área×dia e formato de cada um em
  `docs/formatos.md`. Site institucional é canal da marca mas ainda sem
  calendário/formato definidos aqui. WhatsApp e telefone como contato
  direto (permitido pela Pergunta 04 da Cartilha OAB — ver
  `docs/normas-oab.md`).
- **E-mail de contato**: financeiro@gutmannesilva.com.br (uso administrativo
  interno; não necessariamente o canal público de contato do escritório —
  confirmar com o time antes de publicar em peça voltada ao público).

## Advogados revisores por área

Desde 2026-09-08, cada post publicado no Notion registra automaticamente o
nome do(s) advogado(s) revisor(es) da área, no campo `Advogados revisores`
do banco "Posts" (ver `docs/notion.md`) — **apenas o nome**, sem disparo de
e-mail, Slack ou WhatsApp: é o time que confere o Notion, não uma
notificação ativa (ver "Fora de escopo" em `CLAUDE.md`). Levantamento feito
por formulário interno em 2026-08-31; mais de uma pessoa por área é
intencional — todas aparecem no campo, sem ordem de prioridade entre elas:

| Área | Advogado(s) revisor(es) |
|---|---|
| Empresarial | Ricardo Gonçalves |
| Cível (todos os 5 subtemas) | Ricardo Gonçalves, Karin Barbosa Joaquim, Aline Cristina Rivolli, Kethlyn Cristina Pereira, Matheus Gutmann |
| Trabalhista | Grazielle Foltran, Fernanda Maria Alves Ferreira, Clayton Jose Batista, Gabriela Munhoz Lacerda, Daiane Baia |
| Tributário | Amanda Camilo, Larissa |
| Previdenciário | Larissa |

Previdenciário não teve resposta no formulário original — Larissa foi
designada manualmente pelo escritório em 2026-09-08, além de Tributário.
Atualize esta tabela diretamente (não há automação para recolher o
formulário de novo) se alguém entrar, sair, ou mudar de área.

## Público-alvo

Desde 2026-08-17, público-alvo se define primeiro por **canal**, depois por
área (ver `docs/formatos.md` para a divisão de área×dia×formato de cada
canal):

- **LinkedIn — pessoa jurídica, exclusivamente.** Gestores, sócios,
  jurídico interno, RH e financeiro de empresas. O canal existe para
  atrair empresas e reforçar o escritório como referência técnica — por
  isso só cobre as 3 áreas inerentemente B2B (Empresarial, Trabalhista pelo
  ângulo empregador, Tributário). Podem ter vocabulário de negócios
  desenvolvido, mas não necessariamente jurídico. Prioridade: relevância
  prática para quem decide na empresa — o que muda na operação, no risco,
  na gestão.
- **Instagram — misto, por área.** Pessoa física (Cível — incluindo o
  subtema Família —, Previdenciário, parte de Trabalhista): público leigo,
  sem vocabulário
  jurídico prévio. Prioridade: clareza acima de precisão técnica
  exaustiva — precisão não pode ser sacrificada, mas o texto precisa ser
  lido por quem nunca abriu um código. Pessoa jurídica (Empresarial,
  Tributário, parte de Trabalhista): mesmo público de negócios do LinkedIn,
  mas em registro mais curto e didático (ver `docs/formatos.md`).

## Tom de voz

- **Sóbrio e informativo**, nunca alarmista. Consequência direta da
  Pergunta 07 da Cartilha (propósito exclusivamente ilustrativo/educacional)
  e da regra transversal de sobriedade e discrição do Provimento 205/2021.
- **Didático sem ser condescendente**: explica o termo técnico na primeira
  aparição, não repete a explicação a cada peça.
- **Terceira pessoa institucional** ("o escritório", "a equipe") em vez de
  primeira pessoa do singular — evita a sensação de promoção pessoal de um
  advogado específico, o que também ajuda a manter a Pergunta 07 em dia.
- **Frases curtas nas peças de mídia social** (carrossel, stories, reel);
  registro mais analítico e com parágrafos completos apenas no formato
  LinkedIn (ver `docs/formatos.md`).
- **LinkedIn especificamente é registro de autoridade técnica corporativa**
  (ver "Registro: dois subtipos" em `docs/formatos.md`) — cita dispositivo
  legal com precisão, compara antes/depois da norma, usa framing de risco e
  gestão para quem decide na empresa. O fechamento pode identificar a
  especialidade do escritório na área do post (permitido pela Pergunta 08),
  sempre sóbrio — nomear "atua em Direito Empresarial" é diferente de
  "somos referência em Direito Empresarial". O primeiro é informação; o
  segundo é autoelogio vedado pela Pergunta 07. Autoridade se constrói pela
  precisão e profundidade da análise, nunca pela afirmação da própria
  competência.
- **Nunca**: urgência, superlativos automráticos ("o melhor", "líder"),
  garantia de resultado, menção a caso real de cliente. Ver checklist
  completo em `docs/normas-oab.md`.

## O que cada área tende a cobrir

Estas são linhas editoriais amplas — os temas específicos de cada semana
vêm de `temas/<area>.md`, não daqui.

- **Empresarial**: contratos, societário, compliance, regulação de
  atividade econômica, mudanças legislativas que afetam operação de
  empresas.
- **Cível**: guarda-chuva de 5 subtemas, cada um com o próprio banco em
  `temas/civel/<subtema>.md` (ver `docs/formatos.md`, seção "Cível —
  subtemas"):
  - **Imobiliário**: locação, condomínio, relações de vizinhança.
  - **Família**: casamento, união estável, divórcio, guarda, herança,
    planejamento sucessório. Subárea sensível: exige atenção redobrada às
    Regras 1 e 2 do checklist (nada de promessa de resultado nem menção a
    caso concreto).
  - **Responsabilidade Civil**: dano moral, indenização, responsabilidade
    de plataformas digitais.
  - **Direito das Coisas**: posse, propriedade, usucapião.
  - **Contratos**: contratos entre particulares, direito do consumidor,
    cláusulas abusivas.
- **Trabalhista**: direitos e deveres na relação de emprego, mudanças na
  CLT e normas correlatas, jornada, rescisão — sempre em nível informativo,
  nunca como consultoria para caso individual. Cada tema do banco
  (`temas/trabalhista.md`) indica o ângulo predominante — reclamante,
  reclamado ou ambos — mas o arquivo continua único, sem subpastas.
- **Tributário**: tributos federais/estaduais/municipais, obrigações
  acessórias, parcelamentos, reformas tributárias em tramitação ou vigor,
  isenções (ex.: Imposto de Renda).
- **Previdenciário**: benefícios do INSS, aposentadoria, mudanças em regras
  previdenciárias, direitos de segurados.

## Assinatura visual (referência para a seção de design dos briefings)

- Paleta e identidade visual seguem o manual de marca do escritório
  (arquivo fora deste repositório — a automação não define paleta nova, só
  referencia "seguir manual de marca" na seção de design de cada briefing).
- Logotipo do escritório: permitido (Pergunta 08). Símbolo/logotipo da OAB:
  **nunca** (Pergunta 13).
