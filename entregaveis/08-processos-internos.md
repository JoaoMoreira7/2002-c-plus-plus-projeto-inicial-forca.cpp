# Processos Internos — CRM, Fluxo de Atendimento e Modelo de Proposta
> Produzido pelo agente `consultor-administrativo`
> Objetivo: dar à JM NFE uma máquina interna padronizada que sustenta a escala (Fase 2/3).

---

## 1. Fluxo de atendimento (lead → entrega)

```
[1] CAPTAÇÃO         → lead chega (site, WhatsApp, indicação, conteúdo)
        ↓
[2] QUALIFICAÇÃO     → é o cliente certo? (tipo, demanda, urgência, capacidade)
        ↓
[3] DIAGNÓSTICO      → entender o caso; coletar documentos mínimos
        ↓
[4] PROPOSTA         → escopo + prazo + preço (modelo padrão, item 4)
        ↓
[5] CONTRATO         → assinatura + coleta LGPD (base legal + termo)
        ↓
[6] EXECUÇÃO         → cálculo/laudo/consultoria (checklist do serviço)
        ↓
[7] REVISÃO (QC)     → reconferência por 2º método; conformidade
        ↓
[8] ENTREGA          → laudo/parecer + reunião de devolutiva
        ↓
[9] PÓS / RECORRÊNCIA→ follow-up, NPS, oportunidade de subir na escada
```

**Donos e prazos (SLA sugerido):**
| Etapa | Responsável | Prazo-alvo |
|---|---|---|
| Resposta ao lead | Atendimento | até 4h úteis |
| Qualificação + diagnóstico | Técnico/sócio | 1–2 dias |
| Proposta enviada | Comercial | 1 dia após diagnóstico |
| Execução | Perito/consultor | conforme escopo |
| Revisão QC | 2º revisor | antes de toda entrega |

---

## 2. CRM — estrutura mínima (pode começar em planilha/Notion/Trello)

**Cada lead/cliente é um registro com:**
| Campo | Exemplo |
|---|---|
| ID / Nome | 2026-0001 / Dr. Fulano |
| Origem | Indicação / Site / WhatsApp / Conteúdo |
| Tipo | Advogado · Escritório · Empresa · Trabalhador · Contabilidade |
| Demanda | Liquidação · Revisão · Auditoria · Consultoria · IA |
| Estágio | Lead · Qualificado · Proposta · Fechado · Perdido · Cliente |
| Valor estimado | R$ |
| Probabilidade | % |
| Próxima ação + data | "Enviar proposta — 05/06" |
| Responsável | — |
| Observações / histórico | — |

**Funil (estágios) e meta:** medir taxa de conversão entre estágios (lead→proposta→
fechado). Acione `dados-analytics` para acompanhar. **Recorrência** (parceiros) tem visão
própria: nº de demandas/mês por parceiro.

**Automação simples (Fase 3 com `arquiteto-software`/`devops-sre`):**
- WhatsApp/formulário cria o registro automaticamente.
- Lembrete de "próxima ação" vencida.
- Modelo de proposta gerado a partir dos dados do registro.

---

## 3. Banco de documentos (padronização)

Estrutura de pastas sugerida (por cliente e por tipo):
```
/clientes/{ano}-{id}-{nome}/
    /01-diagnostico/       (documentos recebidos: sentença, holerites, extratos)
    /02-proposta-contrato/
    /03-execucao/          (planilhas de cálculo, rascunhos)
    /04-entrega/           (laudo/parecer final assinado)
    /05-comunicacao/
/modelos/                  (templates — itens abaixo)
    laudo.docx · parecer.docx · proposta.docx · contrato.docx · termo-lgpd.docx
    checklist-liquidacao.pdf · planilhas .xlsx (entregáveis 05 e 07)
```
**Regra LGPD:** dados de processo/holerite são pessoais (parte, sensíveis) → acesso
restrito, retenção definida, descarte seguro ao fim do prazo. Política escrita.

---

## 4. Modelo de proposta comercial (template)

> **PROPOSTA TÉCNICA Nº ____/2026 — JM NFE Consultoria**
>
> **Cliente:** __________  **Data:** __/__/____  **Validade:** 15 dias
>
> **1. Contexto / problema**
> _(1–3 frases descrevendo a dor do cliente, na linguagem dele)_
>
> **2. Escopo do serviço**
> _(o que será feito, objetivamente — ex.: "Revisão técnica dos cálculos de liquidação do
> processo nº ___, com parecer de assistente técnico e memória de cálculo.")_
> Inclui: __________   |   Não inclui: __________
>
> **3. Entregáveis**
> _(ex.: parecer técnico + planilha de cálculo + reunião de devolutiva)_
>
> **4. Prazo**
> _(ex.: 7 dias úteis após o recebimento dos documentos)_
>
> **5. Investimento**
> R$ __________  | Forma de pagamento: __________
> _(Para perícia por nomeação judicial, os honorários seguem regra própria do juízo —
> não confundir com contratação privada.)_
>
> **6. Condições**
> _(documentos necessários, responsabilidades das partes, sigilo/LGPD)_
>
> **Observações de conformidade (não remover):** serviço de natureza técnica; não constitui
> advocacia nem garante resultado judicial. _(Revisão por `juridico-compliance`.)_

---

## 5. Checklists internos (qualidade)

**Checklist de abertura de caso**
- [ ] Cliente qualificado e tipo registrado no CRM.
- [ ] Documentos mínimos recebidos e arquivados em /01-diagnostico.
- [ ] Termo LGPD assinado (base legal definida).
- [ ] Proposta/contrato assinados.

**Checklist de entrega (QC)**
- [ ] Checklist do serviço (ex.: liquidação) 100% cumprido.
- [ ] Reconferência por 2º método feita.
- [ ] Conformidade revisada (sem manifestação jurídica indevida; sem dado exposto).
- [ ] Memória/fontes registradas; arquivo final em /04-entrega.

---

## 6. Indicadores internos (poucos e úteis)
| KPI | Para quê |
|---|---|
| Taxa de conversão (lead→fechado) | Saúde comercial |
| Tempo médio de execução por serviço | Capacidade / preço |
| Receita recorrente (parceiros) | Previsibilidade (Fase 2) |
| Retrabalho / impugnações sofridas | Qualidade técnica |
| NPS / satisfação | Fidelização |

---

## 7. Roteiro de implantação (incremental — não tudo de uma vez)
1. **Semana 1–2:** CRM em planilha + pastas padronizadas + termo LGPD.
2. **Semana 3–4:** modelos de proposta/contrato/laudo + checklists.
3. **Mês 2:** SLA de atendimento + KPIs no CRM.
4. **Fase 3:** automações e sistema próprio (com o time de tecnologia/IA).
