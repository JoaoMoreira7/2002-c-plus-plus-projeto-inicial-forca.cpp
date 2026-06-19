# Tabelas Vigentes 2026 + Metodologia de Índice por Período
> Produzido pelo agente `perito-calculista-trabalhista`
> Regra-mãe: **o índice segue o PERÍODO dos autos e a DECISÃO LIQUIDANDA** — nunca um
> número fixo "de cabeça". Este documento orienta o agente a buscar o índice correto de
> cada competência na fonte oficial.

---

## 1. Como o agente trata índices por período (o requisito central)

Cálculo trabalhista se atualiza **mês a mês (por competência)**. O fluxo do agente:

1. **Leia a decisão liquidanda.** Ela define os parâmetros — inclusive, muitas vezes, o
   critério de correção/juros. **O que a sentença/acórdão determina prevalece.**
2. **Identifique o período de cada parcela** (competência de origem) e a **data-base** do
   cálculo (até quando atualizar).
3. **Determine a fase** de cada intervalo (ver item 2): pré-judicial × a partir do ajuizamento.
4. **Busque o índice oficial de cada competência** na fonte (item 4) — IPCA-E, SELIC ou a
   tabela única do TRT/CSJT já consolidada.
5. **Aplique por competência** (a planilha avançada `07` faz o lookup por data).
6. **Registre fonte e data** de cada índice na aba Memória. Reconfira.

> ⚠️ IPCA-E e SELIC são **pós-fixados**: o índice de um mês só existe depois de fechado.
> Para meses muito recentes, use o critério/projeção que a Justiça do Trabalho adotar e
> sinalize a provisoriedade.

---

## 2. Critério de correção monetária e juros — débito trabalhista (vigente)

> Resumo para orientar; **sempre confirmar a decisão do caso e a tabela oficial atual.**

- **ADC 58/59 (STF, dez/2020):** enquanto não houver lei específica, aplica-se:
  - **Fase pré-judicial** (antes do ajuizamento): **IPCA-E** + juros de mora legais.
  - **A partir do ajuizamento:** **SELIC** (que já engloba correção + juros — não cumular
    com outro índice nem com juros à parte).
- **Lei 14.905/2024** (vigência a partir de ~ago/2024): alterou o **Código Civil** (IPCA
  como correção e SELIC como juros para obrigações civis). **Não alterou a CLT** — há
  **divergência** sobre sua aplicação ao crédito trabalhista. O TST/tribunais vêm
  consolidando o entendimento; **verifique a posição vigente e a do juízo do caso**.
- **Conclusão prática:** o critério pode mudar conforme **a fase, o período e a decisão**.
  Por isso a planilha trabalha com **tabela de índices por competência**, não com índice fixo.

---

## 3. Tabelas tributárias 2026 (para descontos, quando aplicável)

> ⚠️ Verbas rescisórias têm regras próprias de incidência. Em geral são **isentas de IR**:
> aviso prévio indenizado, férias indenizadas + 1/3, FGTS e multa de 40%. O **13º** tem
> **tributação exclusiva** (separada dos demais rendimentos). INSS não incide sobre verbas
> indenizatórias. **Apure a incidência verba a verba.**

### 3.1 INSS 2026 (Portaria Interministerial MPS/MF nº 13/2026)
- Salário mínimo 2026: **R$ 1.621,00** · Teto do INSS: **R$ 8.475,55**.
- Alíquotas progressivas por faixa: **7,5% · 9% · 12% · 14%** (aplicadas faixa a faixa, ou
  pela fórmula "alíquota da faixa × salário − parcela a deduzir").
- ⚠️ **Limites intermediários e parcelas a deduzir de 2026:** confirmar os valores exatos
  na **Portaria MPS/MF nº 13/2026** antes de usar (a planilha traz esses limites como
  células de entrada, justamente para serem preenchidos da fonte oficial).

### 3.2 IRRF 2026 (reforma do IR)
- **Isenção total** para renda mensal até **R$ 5.000,00**; **redução parcial e decrescente**
  para renda de **R$ 5.000,01 a R$ 7.350,00**; tabela progressiva acima disso.
- ⚠️ As **faixas, alíquotas e parcelas a deduzir exatas** devem ser obtidas na **tabela
  oficial da Receita Federal de 2026** (a mecânica de redutor mensal mudou). Não use
  tabela de anos anteriores.

---

## 4. Fontes oficiais de índices (onde o agente busca)

| Índice / dado | Fonte oficial | Uso |
|---|---|---|
| **Tabela única de atualização** (correção + juros já consolidados) | **TRT da região** (ex.: TRT-2 "Tabelas Práticas") e **CSJT** | Forma mais segura: já vem por competência |
| **IPCA-E** | **IBGE** | Fase pré-judicial |
| **SELIC** (acumulada) | **Banco Central (BACEN)** | A partir do ajuizamento |
| **INSS 2026** | Portaria Interministerial **MPS/MF nº 13/2026** | Desconto previdenciário |
| **IRRF 2026** | **Receita Federal** (tabela oficial 2026) | Desconto de IR |
| **Salário mínimo / pisos** | Decreto federal / CCT da categoria | Bases |

> Boa prática JM NFE: preferir a **tabela única do TRT/CSJT** já consolidada por
> competência — reduz erro de composição de índices. Sempre anotar a **data de extração**
> da tabela (elas são atualizadas mensalmente).

---

## 5. Checklist de índice (antes de fechar o cálculo)
- [ ] Li a decisão liquidanda e respeitei o critério que ela fixa.
- [ ] Identifiquei a competência de cada parcela e a data-base.
- [ ] Separei fase pré-judicial × a partir do ajuizamento.
- [ ] Busquei o índice de CADA competência na fonte oficial (com data de extração).
- [ ] Não cumulei SELIC com outro índice/juros no período em que ela já engloba ambos.
- [ ] Registrei fonte, período e data de cada índice na Memória.
- [ ] Reconferi o total atualizado por método independente.

---

## Fontes consultadas (2026)
- [Tabela INSS 2026 — Serasa Experian](https://www.serasaexperian.com.br/conteudos/tabela-inss-2026/)
- [Tabela INSS 2026 — Contabilizei](https://www.contabilizei.com.br/contabilidade-online/tabela-inss/)
- [Tabela IR 2026 — Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/veja-faixas-e-aliquotas-das-novas-tabelas-do-imposto-de-renda-2026)
- [Nova Tabela do IR 2026 — gov.br/Secom](https://www.gov.br/secom/pt-br/assuntos/noticias/2026/01/nova-tabela-do-ir-veja-faixas-e-aliquotas-e-saiba-mais-sobre-medida-que-isenta-o-pagamento-para-quem-ganha-ate-r-5-mil)
- [STF: IPCA-E e SELIC para débitos trabalhistas (ADC 58) — TST](https://www.tst.jus.br/-/stf-define-que-ipca-e-e-selic-devem-ser-aplicados-para-corre%C3%A7%C3%A3o-monet%C3%A1ria-de-d%C3%A9bitos-trabalhistas)
- [Atualização de débitos trabalhistas — TRT-2 (Tabelas Práticas)](https://ww2.trt2.jus.br/servicos/consultas/tabelas-praticas/atualizacao-de-debitos-trabalhistas)
- [Nova sistemática de correção e juros trabalhistas — Jusbrasil](https://www.jusbrasil.com.br/artigos/a-nova-sistematica-de-correcao-monetaria-e-juros-para-os-debitos-trabalhistas/1496937376)

> Observação de conformidade: este material é técnico e de apoio; não constitui parecer
> jurídico. Os valores/critérios mudam — confirmar sempre na fonte oficial e na decisão do caso.
