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
- **Nada foi publicado no Notion.**
- `Status` de cada peça está como "Rascunho — teste", não "Em aprovação".

Se o usuário aprovar o conteúdo e quiser transformar isso na semana
oficial: mover para `calendarios/2026-S38/` (ajustando nomes de arquivo se
o rodízio tiver avançado nesse meio-tempo), atualizar
`temas/historico.md`, publicar no Notion e então apagar esta pasta e este
aviso.

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

## ⚠️ Efeito colateral notado no algoritmo (reportar ao usuário)

**3 dos 5 posts do Instagram desta semana caíram no mesmo formato — Reel
rápido** (Empresarial, Cível e Trabalhista, todos com contador = 3). Isso
acontece porque o histórico atual (S34-S36) é simétrico: cada uma das 5
áreas já usou exatamente 1 Carrossel, 1 Post estático e 1 Reel, uma vez
cada, nas 3 semanas antigas — então todas chegam ao rodízio de 6 formatos
no mesmo ponto (índice 3) ao mesmo tempo. É uma consequência correta do
algoritmo como documentado, não um bug de implementação — mas o resultado
prático (3 Reels na mesma semana) contraria o próprio objetivo de variar
formato que motivou ir de 3 para 6 formatos.

**Não apliquei o "Desvio editorial do rodízio de formato" para corrigir
isso** — esse desvio é para quando o *tema* não cabe no formato sorteado,
não para evitar coincidência entre trilhas diferentes; usá-lo aqui seria
inventar uma regra nova sem autorização. Fica como observação para o
usuário decidir se quer um ajuste permanente (ver sugestão na mensagem de
resposta).
