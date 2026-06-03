# Extrator de Liquidação (IA) — JM NFE
> Braço de Tecnologia + IA. O Agente lê o **PDF inteiro** do processo e extrai os
> dados necessários para a liquidação, em JSON estruturado + relatório de conferência.
> Construído com a Claude API (`claude-opus-4-8`) e saída estruturada validada por schema.

## O que faz
1. Lê o PDF (texto via `pdfplumber`; ou o PDF nativo, para escaneados).
2. Envia ao modelo com instruções de **método pericial** e schema de saída.
3. Devolve:
   - `*_extracao.json` — dados estruturados (processo, partes, contrato, ajuizamento,
     verbas deferidas com período/reflexos, FGTS, critério de correção/juros, fontes).
   - `*_relatorio.md` — relatório legível com **trechos-fonte** e **checklist de revisão**.
   - (opcional) cópia da **planilha 07** com a aba `Verbas` e a `Memoria` pré-preenchidas.

## Princípio inegociável: a IA PROPÕE, o PERITO DECIDE
- **Zero invenção:** só extrai o que está no documento; o que falta vira "campo para revisar".
- **Cita a fonte:** cada dado-chave vem com o trecho literal que o fundamenta.
- **Não fixa índices:** correção/juros seguem a **decisão e o período** — a IA só transcreve
  o critério se a sentença o fixar; senão, marca para o perito confirmar na fonte oficial.
- **Não advoga e não calcula:** apenas prepara os dados para o perito conferir e liquidar.
- **LGPD:** dados do processo são sensíveis — rode em ambiente seguro; não suba PDFs a serviços não autorizados.

## Instalação
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sua-chave"      # obtida no console da Anthropic
```

## Uso
```bash
# Básico (PDF com texto)
python extrator_liquidacao.py processo.pdf

# Saída em pasta + pré-preencher uma cópia da planilha de liquidação
python extrator_liquidacao.py processo.pdf --out ./saida \
    --planilha ../07-planilha-liquidacao-avancada.xlsx

# PDF escaneado (sem texto): envia o PDF ao modelo
python extrator_liquidacao.py processo.pdf --pdf-nativo
```

## Fluxo recomendado (ponta a ponta)
1. Rode o extrator no PDF do processo → confira o `*_relatorio.md` (checklist de revisão).
2. Ajuste/valide os campos no documento (o perito é responsável pelo resultado).
3. Abra a planilha pré-preenchida, lance os **valores históricos por competência** e
   preencha a aba `Indices` com a tabela oficial do período (TRT/CSJT) — ver
   `../06-tabelas-indices-2026-e-metodologia.md`.
4. Reconfira o total por método independente e gere o laudo (`../03-modelo-laudo-pericial.md`).

## Notas técnicas
- **Modelo:** `claude-opus-4-8` (o mais capaz); troque com `--modelo` se necessário.
- **Saída estruturada:** usa `messages.parse()` com schema Pydantic — JSON sempre válido.
- **Prompt caching:** as instruções (system) são cacheadas; em lotes de processos, reduz custo.
- **PDFs grandes:** o modelo tem janela de 1M tokens, mas recorte as peças relevantes
  (sentença/acórdão/cálculos) para economia e foco.
- **Limite:** isto é apoio à decisão; não substitui a perícia nem o parecer jurídico.
```
