# ⚠️ RASCUNHO DE TESTE — não é uma semana oficial

Gerado em 2026-09-13 a pedido do usuário, para testar na prática as regras
criadas nesta mesma sessão: rodízio de área (segunda/quarta/sexta),
Isenção de Imposto de Renda fixa (terça/quinta), 6 formatos no Instagram,
gancho magnético, e citação de lei só na legenda.

**O que isso NÃO é:**
- Não é a pasta oficial `calendarios/2026-S38/` — está em
  `2026-S38-RASCUNHO/` de propósito, para não ser confundida com uma
  semana publicada.
- `temas/historico.md` **não foi atualizado** — os temas escolhidos abaixo
  continuam disponíveis no banco até uma execução real de fato os usar.
- `Status` de cada peça no Notion está como "Rascunho", não em uma etapa
  real do pipeline de produção.

**Atualização de 2026-09-13 — publicado no Notion, como rascunho**: a
pedido do usuário, as 8 páginas + a página de panorama foram publicadas no
Notion (`Status = "Rascunho"`), sob o título "Semana 38 (proposta
alternativa · 5 dias) · 14–18/09" — ver `docs/notion.md` para os links.

**⚠️ Achado importante nessa publicação**: já existia uma página real
"Semana 38 · 14–19/09" no Notion, publicada por outra sessão (~2026-09-07)
usando um esquema **diferente e incompatível** (Instagram de 4 dias, 1 dia
fixo de Isenção de IR, ciclo de 4 semanas, contador global de 3 formatos —
de uma branch nunca mesclada, `claude/instagram-editorial-calendar-notion-6ku7nf`).
Decisão do usuário: manter o esquema deste PR (#6) como o vigente; a
página antiga **não foi apagada nem arquivada** — as duas coexistem no
Notion por enquanto. Ver `docs/notion.md` para o registro completo do
conflito.

**Correção feita durante a publicação**: o Select `Área` do Notion já
tinha uma opção própria `"Isenção de IR"` (criada por aquela outra
sessão) — os posts de terça/quinta foram publicados com `Área = "Isenção
de IR"`, não `"Tributário"` como este repositório assumia antes. Os
arquivos deste rascunho e a documentação (`docs/formatos.md`, `CLAUDE.md`,
`docs/notion.md`, templates) foram corrigidos para refletir isso.

**Atualização de 2026-09-13 — fechamentos corrigidos**: os 8 arquivos
locais e as 8 páginas já publicadas no Notion tiveram o fechamento
reescrito — a fórmula fixa "O escritório atua em Direito X.", repetida
sem variação em todo post, foi apontada pelo usuário como um dos motivos
dos CTAs estarem ruins (ver `docs/perfil-escritorio.md`, "Fechamento e
identificação — variar, nunca repetir fórmula"). Local e Notion estão
sincronizados.

Se o usuário aprovar o conteúdo e quiser transformar isso na semana
oficial: mover para `calendarios/2026-S38/` (ajustando nomes de arquivo se
o rodízio tiver avançado nesse meio-tempo), atualizar
`temas/historico.md`, avançar o `Status` das páginas no pipeline real, e
decidir o que fazer com a página conflitante antiga.

## Cálculo usado (para auditoria)

- Semana ISO alvo: **2026-S38** (segunda 2026-09-14 a sexta 2026-09-18) —
  próxima semana completa a partir de hoje, 2026-09-13.
- Rodízio de área (seg/qua/sex): `p = (3 × (38 − 38)) mod 5 = 0` →
  Segunda = Empresarial, Quarta = Cível, Quinta *(não se aplica, é
  Isenção de IR)*, Sexta = Trabalhista.
- Contadores de formato por trilha, a partir de `temas/historico.md` (17
  linhas de Instagram, nenhuma delas de Isenção de IR ainda):
  - Empresarial: 3 posts anteriores → `3 mod 6 = 3` → **Reel rápido**.
  - Cível (contando `Cível` e `Cível (subtema Imobiliário)`): 3 → `3 mod 6
    = 3` → **Reel rápido**.
  - Trabalhista: 3 → `3 mod 6 = 3` → **Reel rápido**.
  - Isenção de IR: 0 (terça) → `0 mod 6 = 0` → **Carrossel curto**; 1
    (quinta, incrementado) → `1 mod 6 = 1` → **Carrossel padrão**.
- Contador de subtipo do LinkedIn: 9 posts de LinkedIn já publicados →
  próximos 3 contadores são 10, 11, 12 → `mod 5` = 0, 1, 2 → **Autoridade
  técnica** nos 3 posts desta semana.
- Cível: primeiro tema elegível na fila concatenada dos 5 arquivos
  (`imobiliario` → `familia` → `responsabilidade-civil` →
  `direito-das-coisas` → `contratos`) é `imobiliario.md` item 2
  ("Contratos de locação residencial"), porque o item 1 já foi usado em
  2026-S36.

## ⚠️→✅ Efeito colateral notado e corrigido durante o teste

**Achado original**: 3 dos 5 posts do Instagram desta semana caíam no
mesmo formato — Reel rápido (Empresarial, Cível e Trabalhista, todos com
contador = 3). Isso acontecia porque o histórico atual (S34-S36) é
simétrico: cada uma das 5 áreas já usou exatamente 1 Carrossel, 1 Post
estático e 1 Reel, uma vez cada, nas 3 semanas antigas — então todas
chegavam ao rodízio de 6 formatos no mesmo ponto (índice 3) ao mesmo
tempo. Consequência correta do algoritmo como documentado até então, não
um bug de implementação — mas o resultado prático (3 Reels na mesma
semana) contrariava o próprio objetivo de variar formato que motivou ir de
3 para 6 formatos.

**Correção aplicada** (a pedido do usuário): nova regra "Desempate por
colisão entre trilhas na mesma semana" em `docs/formatos.md` — calcule os
5 formatos na ordem do calendário (segunda→terça→quarta→quinta→sexta); se
um formato colidir com o de outro post já calculado **na mesma semana**,
avance para o próximo índice da lista (mod 6) ainda não usado nela.

**Validação adicional — regra de "formato esquecido"**: depois desta
sessão, foi criada uma segunda regra em `docs/formatos.md` para cobrir o
caso "por que não teve Post estático esta semana?" — cobertura mínima
entre trilhas (jejum ≥ 6 força o formato para dentro da semana). Checando
o histórico real (17 linhas de Instagram em `temas/historico.md`, sem
contar esta semana de teste): `Carrossel curto`, `Reel rápido` e
`Carrossel aprofundado` nunca haviam sido usados (jejum infinito — são
formatos novos desta sessão); `Carrossel padrão` tinha jejum 3; `Reel
aprofundado` tinha jejum 1; **`Post estático` tinha jejum 0** (foi
literalmente o último post real publicado, 2026-S36, Previdenciário,
09-05). O resultado desta semana, depois do desempate por colisão, já
cobre os 3 formatos nunca usados + os 2 com maior jejum — deixando de fora
exatamente o único que tinha jejum zero (Post estático). Ou seja: **o
resultado abaixo já está correto também sob a nova regra**, sem precisar
reescrever nenhum arquivo — a ausência de Post estático nesta semana
específica é o resultado certo, não uma falha.

Aplicando a regra de desempate a esta semana:
- Segunda (Empresarial, índice 3 = Reel rápido) — primeiro post, sem
  colisão possível, mantém.
- Terça (Isenção de IR, índice 0 = Carrossel curto) — único até aqui,
  mantém.
- Quarta (Cível, índice 3 = Reel rápido) — **colide com Segunda** → avança
  para índice 4 = **Reel aprofundado** (livre).
- Quinta (Isenção de IR, índice 1 = Carrossel padrão) — único até aqui,
  mantém.
- Sexta (Trabalhista, índice 3 = Reel rápido) — **colide com Segunda** →
  tenta índice 4 (Reel aprofundado), **também ocupado por Quarta** → avança
  para índice 5 = **Carrossel aprofundado** (livre).

Resultado final da semana: Reel rápido, Carrossel curto, Reel aprofundado,
Carrossel padrão, Carrossel aprofundado — **5 formatos diferentes em 5
posts**, o oposto do problema original. Os briefings de Quarta
(`instagram/03-quarta-civel.md`) e Sexta
(`instagram/05-sexta-trabalhista.md`) foram regravados com copy adequada
ao novo formato (roteiro de 30-45s e carrossel de 7 slides,
respectivamente) — a legenda de ambos não mudou de conteúdo técnico, só a
peça visual.
