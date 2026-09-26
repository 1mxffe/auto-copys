# Site institucional — Gutmann & Silva

Página única, estática, sem dependências de build: `index.html` com CSS e JS
inline. Tipografia via Google Fonts (Newsreader + IBM Plex Sans), com
fallback para Georgia/Helvetica. Tem modo escuro automático
(`prefers-color-scheme`).

Para visualizar, abra `index.html` no navegador. Para publicar, basta
servir a pasta em qualquer hospedagem estática.

## Pendências antes de publicar

Os campos abaixo estão com texto provisório (em cinza, marcados com
`class="pending"` e `data-pending="..."` no HTML). Nenhum dado foi
inventado — é preciso preencher com as informações reais:

| Campo | Onde |
|---|---|
| Endereço completo, cidade/UF, CEP | § 4 Contato |
| Horário de atendimento | § 4 Contato |
| E-mail público (o `financeiro@` é interno — ver `docs/perfil-escritorio.md`) | § 4 Contato |
| Telefone e link do WhatsApp | § 4 Contato |
| Número de registro da sociedade na OAB/UF | Rodapé |

Depois de preencher, remova a classe `pending` do elemento para o texto
voltar à cor normal.

Seção de sócios/equipe não foi incluída por falta de dados (nomes, títulos
acadêmicos, inscrições). Títulos, distinções e idiomas são permitidos pela
Pergunta 08 de `docs/normas-oab.md`.

## Conformidade OAB

O texto foi escrito contra o checklist de `docs/normas-oab.md`: sem
promessa de resultado, sem menção a casos ou clientes, sem CTA de
conversão (o contato é só identificação e meio de contato), sem
honorários, sem superlativos ("o melhor", "referência") e sem símbolo da
OAB. Qualquer alteração de copy deve passar pelo mesmo checklist.
