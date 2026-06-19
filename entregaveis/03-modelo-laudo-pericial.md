# Modelo de Laudo/Parecer Pericial + Checklist de Liquidação Trabalhista
> Produzido pelo agente `perito-calculista-trabalhista`
> Uso: TEMPLATE padronizado da JM NFE. Adaptar a cada caso.
> Princípio reitor: **o cálculo é prova** — tudo rastreável, conferido e auditável.

> ⚠️ Avisos obrigatórios:
> - Este é um **modelo de estrutura**, não um cálculo pronto. Índices, alíquotas, tabelas
>   (INSS/IRRF) e critérios de atualização **mudam** e devem ser confirmados na fonte
>   vigente para cada caso.
> - O perito produz **prova técnica**; tese e peça jurídica são privativas de advogado
>   (Lei 8.906/94). Deixe claro o papel (perito do juízo x assistente técnico).
> - Dados do trabalhador/processo são pessoais (parte sensíveis) — sigilo e LGPD.

---

## PARTE A — MODELO DE LAUDO / PARECER

### 1. Identificação
- **Tipo de peça:** ( ) Laudo pericial (perito nomeado) ( ) Parecer de assistente técnico
- **Processo nº / Vara / Comarca:** __________
- **Partes:** Reclamante __________ × Reclamada __________
- **Nomeação / contratante:** __________ (data: ___)
- **Responsável técnico (JM NFE):** __________

### 2. Objeto
Descrever, em uma frase, o que está sendo apurado (ex.: "liquidação da sentença conforme
os parâmetros do dispositivo de fls. ___" ou "análise crítica do laudo oficial de fls. ___").

### 3. Documentos e fontes analisados
Listar TODOS, com folhas/fonte e data:
- [ ] Sentença/acórdão (dispositivo e fundamentação relevante) — fls. ___
- [ ] Contrato de trabalho / CTPS / admissão e rescisão
- [ ] Holerites / fichas financeiras — competências ___ a ___
- [ ] TRCT, extrato de FGTS, guias
- [ ] CCT/ACT aplicável (vigências)
- [ ] Cálculos da parte contrária (se houver impugnação)

### 4. Premissas adotadas (cada uma com fonte e data)
Tabela obrigatória — nenhuma premissa "de cabeça":
| Premissa | Valor/critério adotado | Fonte | Data/competência |
|---|---|---|---|
| Período do contrato / vínculo | | sentença/CTPS | |
| Remuneração-base | | holerite/CCT | |
| Verbas deferidas | | dispositivo da sentença | |
| Base de cálculo de cada verba | | CLT/CCT | |
| Reflexos aplicáveis | | sentença/habitualidade | |
| Critério de **correção monetária** | *(confirmar vigente)* | legislação/decisão | |
| Critério de **juros** | *(confirmar vigente)* | legislação/decisão | |
| FGTS + multa rescisória | | extrato/sentença | |
| Descontos (INSS/IRRF) | *(tabela vigente)* | norma do período | |

### 5. Metodologia
Declarar: ordem de apuração, software/planilha utilizada, e que **o resultado foi
reconferido por método independente**. (Boa prática JM NFE: recalcular por caminho
alternativo + análise de sensibilidade nas premissas-chave.)

### 6. Memória de cálculo (detalhada, parcela a parcela)
Para CADA verba: base × parâmetro = valor histórico → atualização → valor corrigido.
Apresentar de forma que qualquer terceiro reproduza a conta. Subtotais por grupo
(verbas, reflexos, FGTS, atualização) e **total geral**.

### 7. Resposta aos quesitos (se houver)
Quesito → resposta técnica objetiva, fundamentada na memória de cálculo.

### 8. Conclusão
- Valor total apurado: R$ __________ (data-base: ___)
- Em impugnação: divergência apontada vs. cálculo da parte contrária, com a causa do erro.
- **Ressalvas:** premissas a confirmar, documentos faltantes, limites da análise.

### 9. Encerramento
Local, data, assinatura e identificação do responsável técnico.
> *Trabalho de natureza técnica; não constitui manifestação jurídica.*

---

## PARTE B — CHECKLIST DE LIQUIDAÇÃO TRABALHISTA

### Antes de calcular
- [ ] Li o **dispositivo da sentença** e listei TODAS as verbas deferidas.
- [ ] Identifiquei período, jornada e remuneração-base com documento.
- [ ] Reuni holerites/TRCT/extrato de FGTS das competências necessárias.
- [ ] Verifiquei a **CCT/ACT** aplicável e suas vigências.
- [ ] Confirmei o **critério de correção monetária e juros vigente** para a fase.

### Durante o cálculo
- [ ] Base de cálculo correta para cada verba (13º, férias+1/3, aviso, HE...).
- [ ] **Reflexos** aplicados nas parcelas habituais.
- [ ] FGTS: depósitos do período + multa de 40% sobre a base certa.
- [ ] Descontos (INSS/IRRF) com a **tabela do período/regime correto**.
- [ ] Atualização aplicada por competência, não em bloco indevido.

### Depois de calcular (controle de qualidade JM NFE)
- [ ] **Reconferi por método independente** (2ª via do cálculo).
- [ ] Análise de sensibilidade: testei a premissa que mais muda o total.
- [ ] Memória de cálculo reproduzível por terceiro.
- [ ] Todas as premissas têm fonte e data citadas.
- [ ] Ressalvas e documentos faltantes registrados.

### Conformidade
- [ ] Papel declarado (perito x assistente técnico).
- [ ] Nada de manifestação jurídica indevida.
- [ ] Dados pessoais protegidos (sigilo/LGPD).

---

## Como evoluir este modelo (Fase 3 — escala)
- Transformar o checklist em **formulário/sistema** (com `arquiteto-software` + `devops-sre`).
- Planilha-modelo com fórmulas travadas e campos de premissa (reduz erro humano).
- IA para conferência cruzada de holerites e pré-preenchimento — sempre com **revisão
  humana do perito** antes de assinar (a responsabilidade técnica é da pessoa, não da IA).
