# Schema do `posts.json` — dado estruturado por semana

A partir da Semana 2026-S35, cada pasta `calendarios/AAAA-SNN/` passa a
ter, além do `calendario.md` e dos briefings em Markdown, um
`posts.json` — versão estruturada só dos campos de **texto visual e de
legenda** dos 6 posts de Instagram daquela semana. É esse arquivo que o
plugin do Figma (`figma-plugin/`, ver `docs/templates-figma.md`) consome.

O Markdown continua sendo a fonte da verdade e a peça de revisão humana
(é nele que vive o diagnóstico, o checklist OAB, os elementos de design).
O `posts.json` é derivado dele — um recorte só do necessário para
popular template, sem repetir o resto do briefing.

> Só Instagram — o LinkedIn não tem arte, então não entra no
> `posts.json` (ver `docs/formatos.md`).

## Formato

```json
{
  "semana": "2026-S35",
  "periodo": "24/08–29/08",
  "instagram": [
    {
      "arquivo": "01-segunda-empresarial",
      "dia": "Segunda",
      "data": "2026-08-24",
      "area": "Empresarial",
      "formato": "Post estático",
      "conteudo": { "titulo": "...", "corpo": "..." },
      "legenda": "...",
      "hashtags": ["#tag1", "#tag2"]
    }
  ]
}
```

O campo `conteudo` muda de forma conforme `formato`:

| `formato` | Formato de `conteudo` |
|---|---|
| `"Post estático"` | `{ "titulo": string, "corpo": string }` |
| `"Carrossel"` | `{ "slides": [string, string, string, string, string] }` (sempre 5, na ordem do slide 1 ao 5) |
| `"Reel"` | `{ "roteiro": [{ "tempo": string, "tela": string, "fala": string }, ...] }` (o campo `tela` é o que o plugin usa — é o texto que aparece na tela; `fala`/`tempo` ficam no JSON só de referência, não vão pro Figma) |

`legenda` e `hashtags` valem para os 3 formatos igualmente — são o texto
da publicação do Instagram, não algo que entra na arte.

## Quem gera esse arquivo

O passo 10 da skill `calendario-semanal`
(`.claude/skills/calendario-semanal/SKILL.md`) gera `posts.json` junto
com os outros arquivos da semana, extraindo os mesmos campos que já
escreveu nos briefings em Markdown — não é uma fonte de dado
independente, é um espelho estruturado do que já foi decidido.
