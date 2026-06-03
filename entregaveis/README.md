# Entregáveis — JM NFE Consultoria

Materiais produzidos pelos agentes especialistas (`.claude/agents/`). Todos com guardrails
legais embutidos: sem promessa de resultado, fronteira perícia/advocacia/contabilidade,
índices verificados na fonte vigente e LGPD.

| # | Arquivo | Agente | O que é |
|---|---|---|---|
| 01 | `01-posicionamento-e-site.md` | estrategista-produto + growth-marketing | Posicionamento + copy completa do site |
| 02 | `02-plano-conteudo-fase1.md` | conteudo-seo-juridico | Calendário de 12 temas + 2 artigos prontos |
| 03 | `03-modelo-laudo-pericial.md` | perito-calculista-trabalhista | Template de laudo/parecer + checklist de liquidação |
| 04 | `04-identidade-visual.md` | growth-marketing | Paleta, tipografia, logo, aplicações |
| 05 | `05-planilha-calculo-rescisao.xlsx` | perito-calculista-trabalhista | Planilha de verbas rescisórias (fórmulas protegidas) |
| 06 | `06-tabelas-indices-2026-e-metodologia.md` | perito-calculista-trabalhista | Tabelas 2026 + metodologia de índice por período |
| 07 | `07-planilha-liquidacao-avancada.xlsx` | perito-calculista-trabalhista | Liquidação com **atualização por competência (PROCV)** |
| 08 | `08-processos-internos.md` | consultor-administrativo | CRM, fluxo de atendimento, proposta, checklists |
| 09 | `ferramentas/extrator_liquidacao.py` | perito + tech/IA | Lê o PDF do processo e extrai os dados da liquidação (Claude API) |
| — | `site/` | growth-marketing + design | Site institucional (HTML + CSS) com a identidade |

## Ferramenta de IA (extrator de liquidação)
`ferramentas/extrator_liquidacao.py` lê o **PDF inteiro** do processo e extrai, em JSON
estruturado + relatório de conferência, os dados para a liquidação (partes, contrato,
ajuizamento, verbas com período/reflexos, FGTS, critério de correção/juros — com
trechos-fonte). Pode pré-preencher a planilha 07. Princípio: **a IA propõe, o perito decide**.
Ver `ferramentas/README.md` para instalação (`ANTHROPIC_API_KEY`) e uso.

## Como usar o site
Abra `site/index.html` no navegador. Antes de publicar, substitua os placeholders
`[entre colchetes]` e `55DDDNUMERO` (WhatsApp) por dados reais, e integre o formulário ao
CRM/backend. Conferir o checklist de conformidade do entregável 01.

## Próximos passos sugeridos
- Preencher a aba `Indices` da planilha 07 com a tabela oficial do TRT/CSJT do período.
- Validar tabelas INSS/IRRF 2026 exatas na fonte oficial (Portaria MPS/MF 13/2026; RFB).
- Contratar designer com base no guia 04 (logo + templates).
- Implantar o CRM e os modelos do entregável 08 (incremental).
