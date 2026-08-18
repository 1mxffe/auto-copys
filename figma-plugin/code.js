// Gutmann & Silva — plugin do Figma para popular os templates semanais de
// Instagram a partir do posts.json gerado pela skill calendario-semanal.
//
// Convenção de nomes exigida nos templates — ver docs/templates-figma.md:
//   TEMPLATE_POST_ESTATICO          (texto: "titulo", "corpo")
//   TEMPLATE_CARROSSEL_SLIDE_1..5   (texto: "texto")
//   TEMPLATE_REEL_TELA_1..4         (texto: "texto")
//
// Não testado dentro do Figma nesta sessão (sem acesso ao aplicativo aqui)
// — ver a seção "Testando" de docs/templates-figma.md antes de confiar
// nisto em produção.

figma.showUI(__html__, { width: 340, height: 260 });

const RAW_BASE = "https://raw.githubusercontent.com/1mxffe/auto-copys/main/calendarios";

figma.ui.onmessage = async (msg) => {
  if (msg.type !== "popular") return;

  const semana = (msg.semana || "").trim();
  if (!semana) {
    figma.ui.postMessage({ type: "erro", texto: "Informe a semana (ex.: 2026-S35)." });
    return;
  }

  let dados;
  try {
    const resposta = await fetch(`${RAW_BASE}/${semana}/posts.json`);
    if (!resposta.ok) {
      throw new Error(`HTTP ${resposta.status} — a semana existe em calendarios/${semana}/posts.json no GitHub?`);
    }
    dados = await resposta.json();
  } catch (erro) {
    figma.ui.postMessage({
      type: "erro",
      texto: `Não consegui buscar posts.json da semana ${semana}: ${erro.message}`,
    });
    return;
  }

  const log = [];
  for (const post of dados.instagram || []) {
    try {
      await popularPost(post, semana);
      log.push(`✅ ${post.arquivo}`);
    } catch (erro) {
      log.push(`⚠️ ${post.arquivo}: ${erro.message}`);
    }
  }

  if (log.length === 0) {
    log.push('Nenhum post de Instagram encontrado em "instagram" no posts.json.');
  }

  figma.ui.postMessage({ type: "resultado", log });
};

async function popularPost(post, semana) {
  if (post.formato === "Post estático") {
    await popularPostEstatico(post, semana);
  } else if (post.formato === "Carrossel") {
    await popularCarrossel(post, semana);
  } else if (post.formato === "Reel") {
    await popularReel(post, semana);
  } else {
    throw new Error(`formato "${post.formato}" não reconhecido`);
  }
}

function acharTemplate(nome) {
  const node = figma.currentPage.findOne(
    (n) => n.name === nome && (n.type === "FRAME" || n.type === "COMPONENT")
  );
  if (!node) {
    throw new Error(`template "${nome}" não encontrado na página atual (conferir docs/templates-figma.md)`);
  }
  return node;
}

function acharTextoNoFrame(frame, nomeCamada) {
  const node = frame.findOne((n) => n.type === "TEXT" && n.name === nomeCamada);
  if (!node) {
    throw new Error(`camada de texto "${nomeCamada}" não encontrada dentro de "${frame.name}"`);
  }
  return node;
}

async function definirTexto(frame, nomeCamada, texto) {
  const textNode = acharTextoNoFrame(frame, nomeCamada);
  // Uma camada de texto pode ter múltiplos "font segments" (trechos com
  // fontes diferentes) — carregar todas antes de sobrescrever o conteúdo,
  // ou a API rejeita a escrita.
  const fontes = textNode.getRangeAllFontNames(0, textNode.characters.length);
  for (const fonte of fontes) {
    await figma.loadFontAsync(fonte);
  }
  textNode.characters = texto || "";
}

function clonarNomeado(template, novoNome) {
  const clone = template.clone();
  clone.name = novoNome;
  clone.x = template.x + template.width + 200;
  clone.y = template.y;
  figma.currentPage.appendChild(clone);
  return clone;
}

async function popularPostEstatico(post, semana) {
  const template = acharTemplate("TEMPLATE_POST_ESTATICO");
  const clone = clonarNomeado(template, `${semana} · ${post.arquivo}`);
  const conteudo = post.conteudo || {};
  await definirTexto(clone, "titulo", conteudo.titulo);
  await definirTexto(clone, "corpo", conteudo.corpo);
}

async function popularCarrossel(post, semana) {
  const slides = (post.conteudo || {}).slides || [];
  for (let i = 0; i < slides.length; i++) {
    const numero = i + 1;
    const template = acharTemplate(`TEMPLATE_CARROSSEL_SLIDE_${numero}`);
    const clone = clonarNomeado(template, `${semana} · ${post.arquivo} · slide ${numero}`);
    await definirTexto(clone, "texto", slides[i]);
  }
}

async function popularReel(post, semana) {
  const roteiro = (post.conteudo || {}).roteiro || [];
  for (let i = 0; i < roteiro.length; i++) {
    const numero = i + 1;
    let template;
    try {
      template = acharTemplate(`TEMPLATE_REEL_TELA_${numero}`);
    } catch (erro) {
      throw new Error(
        `roteiro tem ${roteiro.length} tela(s), mas não achei "TEMPLATE_REEL_TELA_${numero}" (${erro.message})`
      );
    }
    const clone = clonarNomeado(template, `${semana} · ${post.arquivo} · tela ${numero}`);
    await definirTexto(clone, "texto", roteiro[i].tela);
  }
}
