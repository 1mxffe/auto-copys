# Calendário editorial — Semana 38/2026 (14/09–18/09) — ⚠️ RASCUNHO DE TESTE

> **Isto não é uma semana oficial.** Gerado para testar as regras novas
> (rodízio de área, Isenção de IR fixa, 6 formatos, gancho magnético, lei
> só na legenda). `temas/historico.md` não foi tocado, nada foi publicado
> no Notion. Ver `README-TESTE.md` nesta pasta para o cálculo completo —
> incluindo a regra de desempate por colisão de formato, criada durante
> este mesmo teste depois de o rodízio bruto convergir 3 dos 5 posts para
> o mesmo formato.

## LinkedIn (3 posts)

| Dia | Área | Formato | Subtipo | Tema | Arquivo | Conformidade OAB |
|---|---|---|---|---|---|---|
| Segunda | Empresarial | Texto longo | Autoridade técnica | Contratos de prestação de serviço entre empresas | `linkedin/01-segunda-empresarial.md` | ✅ |
| Quarta | Trabalhista | Texto longo | Autoridade técnica | Acordo individual x convenção coletiva | `linkedin/02-quarta-trabalhista.md` | ✅ |
| Sexta | Tributário | Texto longo | Autoridade técnica | ITCMD em heranças e doações | `linkedin/03-sexta-tributario.md` | ✅ |

## Instagram (5 posts)

Segunda/quarta/sexta em rodízio de área (`p = 0` para esta semana — ver
`README-TESTE.md`); terça/quinta fixos em Isenção de Imposto de Renda.

| Dia | Área | Formato | Tema | Arquivo | Conformidade OAB |
|---|---|---|---|---|---|
| Segunda | Empresarial | Reel rápido | Marcas e propriedade intelectual | `instagram/01-segunda-empresarial.md` | ✅ |
| Terça | Tributário (Isenção de IR) | Carrossel curto | Isenção de IR — doença grave | `instagram/02-terca-isencao-ir.md` | ✅ |
| Quarta | Cível (Imobiliário) | Reel aprofundado *(ajustado — ver nota)* | Contratos de locação residencial | `instagram/03-quarta-civel.md` | ✅ |
| Quinta | Tributário (Isenção de IR) | Carrossel padrão | Isenção de IR — maiores de 65 anos | `instagram/04-quinta-isencao-ir.md` | ✅ |
| Sexta | Trabalhista | Carrossel aprofundado *(ajustado — ver nota)* | Licença-maternidade e paternidade | `instagram/05-sexta-trabalhista.md` | ✅ |

**Nota sobre os ajustes**: o rodízio bruto (contador por trilha, sem
desempate) apontava Reel rápido para Empresarial, Cível *e* Trabalhista
na mesma semana — colisão tripla por simetria do histórico atual. Depois
de reportado, foi criada a regra "Desempate por colisão entre trilhas na
mesma semana" (`docs/formatos.md`) e aplicada aqui: Quarta avança para
Reel aprofundado, Sexta avança (pulando o já ocupado Reel aprofundado)
até Carrossel aprofundado. Ver `README-TESTE.md` para o detalhe.

## Fonte dos temas

Todos os 8 vieram do banco de temas (sem checagem de atualidade jurídica
nesta execução de teste, para manter o resultado reproduzível):
- Empresarial (Instagram): `temas/empresarial.md`, item 7.
- Empresarial (LinkedIn): `temas/empresarial.md`, item 8.
- Trabalhista (Instagram): `temas/trabalhista.md`, item 8.
- Trabalhista (LinkedIn): `temas/trabalhista.md`, item 7.
- Tributário (LinkedIn): `temas/tributario.md`, item 5.
- Cível (Instagram): `temas/civel/imobiliario.md`, item 2.
- Isenção de IR (terça): `temas/tributario-isencao-ir.md`, item 1.
- Isenção de IR (quinta): `temas/tributario-isencao-ir.md`, item 2.

## Publicação no Notion

**Não publicado.** Este é um rascunho de teste — nenhuma página foi criada
no banco "Posts" nem na página Calendário Editorial.

## Pendências / o que ficou de fora

- **Rascunho de teste, não semana oficial**: `temas/historico.md` não foi
  atualizado; Notion não foi tocado. Ver `README-TESTE.md`.
- **Ajuste de formato aplicado durante o teste**: o rodízio bruto convergia
  3 dos 5 posts para Reel rápido (colisão entre trilhas). O usuário pediu
  a correção; foi criada a regra "Desempate por colisão entre trilhas na
  mesma semana" (`docs/formatos.md`) e os posts de Quarta (Cível) e Sexta
  (Trabalhista) foram regravados nos formatos resultantes (Reel
  aprofundado e Carrossel aprofundado, respectivamente).
- **Sem checagem de atualidade jurídica**: todos os 8 temas vieram do
  banco, sem consulta à web, para manter o teste determinístico e
  reproduzível.
