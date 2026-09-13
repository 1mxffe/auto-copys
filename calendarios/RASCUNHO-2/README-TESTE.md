# ⚠️ RASCUNHO DE TESTE — sem numeração de semana, a pedido do usuário

Gerado em 2026-09-13. Diferente do primeiro teste
(`calendarios/2026-S38-RASCUNHO/`), esta pasta **não leva número de
semana no nome** — pedido explícito do usuário, para não confundir com
pastas de semana oficial nem com a numeração já disputada da Semana 38
(ver `docs/notion.md` para o conflito registrado ali).

**Objetivo deste teste**: validar o rodízio ao longo de **várias semanas
seguidas**, não só uma — este é o calendário da semana seguinte à do
primeiro teste (calendário 21–25/09/2026, ISO 2026-S39), calculado como
se aquele primeiro teste tivesse mesmo acontecido.

**Nada disto foi publicado no Notion nem em `temas/historico.md`** — nem
o teste anterior (S38) nem este foram gravados lá; os cálculos abaixo
tratam o conteúdo de `2026-S38-RASCUNHO/` como hipoteticamente publicado
só para efeito de continuidade do rodízio, sem que isso seja verdade em
`temas/historico.md`.

## Cálculo usado (para auditoria)

- Semana ISO usada para os cálculos: **2026-S39** (segunda 21/09 a sexta
  25/09/2026).
- Rodízio de área (seg/qua/sex): `p = (3 × (39 − 38)) mod 5 = 3` → Segunda
  = `LISTA[3]` = Tributário, Quarta = `LISTA[4]` = Previdenciário, Sexta =
  `LISTA[0]` = Empresarial. Cível e Trabalhista ficam fora do rodízio de
  área do Instagram nesta semana (Trabalhista continua aparecendo no
  LinkedIn, como sempre).
- Contadores de formato por trilha, tratando os 8 posts do teste anterior
  (S38-RASCUNHO) como já contados:
  - Tributário: 3 (real) + 0 (não apareceu no Instagram em S38) = 3 →
    `3 mod 6 = 3` → Reel rápido.
  - Previdenciário: 3 + 0 = 3 → `3 mod 6 = 3` → Reel rápido → **colide
    com Tributário** → avança para 4 → Reel aprofundado.
  - Empresarial: 3 (real) + 1 (Instagram, S38) = 4 → `4 mod 6 = 4` → Reel
    aprofundado → **colide com Previdenciário** → avança para 5 →
    Carrossel aprofundado → sem colisão, mantém.
  - Isenção de IR: 0 + 2 (S38, terça e quinta) = 2 (terça desta semana) →
    `2 mod 6 = 2` → Post estático; quinta incrementa para 3 → `3 mod 6 =
    3` → Reel rápido → **colide com Tributário (segunda)** → avança para
    4, ocupado por Previdenciário (antes do avanço) → avança para 5,
    ocupado por Empresarial → avança para 0 (volta ao início da lista) →
    Carrossel curto → sem colisão, mantém.
  - Resultado final, em ordem de calendário: Segunda = Reel rápido, Terça
    = Post estático, Quarta = Reel aprofundado, Quinta = Carrossel
    aprofundado, Sexta = Carrossel curto — **5 formatos diferentes**, e
    cobre justamente o formato (Post estático) que tinha ficado de fora
    do teste anterior. Boa validação de que o sistema se autocorrige ao
    longo de várias semanas.
- Contador de subtipo do LinkedIn: 9 (real) + 3 (S38) = 12 antes desta
  semana. Os 3 posts desta semana incrementam para 13, 14, 15 → `mod 5` =
  3, 4, 0 → **Segunda = Autoridade técnica, Quarta = Informativo direto,
  Sexta = Autoridade técnica**. É a primeira vez, nesta série de testes,
  que a posição 4 (Informativo direto) é sorteada — bom teste desse
  mecanismo também.
- Temas: primeiro elegível na fila de cada banco, tratando os temas
  escolhidos no teste S38 como já usados (mesma lógica de
  `temas/historico.md`, sem gravar nada de fato).
