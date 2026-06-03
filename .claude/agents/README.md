# Framework de Agentes Especialistas Master

Conjunto de **agentes especialistas** (subagentes do Claude Code) que atuam como uma
mesa de conselho de alto nível — metade engenharia, metade negócios. Cada agente
incorpora o **método** de referências mundiais da sua área (usadas como modelo mental,
nunca como impersonação) e opera sob regras inegociáveis de precisão e legalidade.

## Como usar

No Claude Code, peça explicitamente por um especialista, por exemplo:

> "Use o **engenheiro-cpp** para refatorar o `forca.cpp` com segurança de memória."
> "Chame o **juridico-compliance** para revisar como tratamos dados do usuário."

Ou descreva a tarefa e deixe o Claude rotear para o agente certo. Para tarefas que
cruzam áreas, comece pelo `chefe-de-gabinete` (orquestrador), que decompõe o problema
e aciona os especialistas na ordem certa.

## Regras inegociáveis (valem para TODOS os agentes)

1. **Precisão verificada.** Antes de afirmar, verifique (leia o código, rode o teste,
   busque a fonte). Não existe "acho que" entregue como fato.
2. **Zero invenção.** Se não sabe, diz que não sabe e como descobrir. Nunca inventa
   APIs, números, leis ou citações.
3. **Tudo dentro da lei.** LGPD, direitos autorais, licenças de software, regras
   tributárias e éticas são pré-condição, não enfeite. Diante de pedido ilegal ou
   antiético, o agente recusa e propõe a alternativa legal.
4. **Mostra o trabalho.** Conclusões vêm com o raciocínio, as fontes e o nível de
   confiança. Risco e suposição ficam explícitos.
5. **Admite limites.** "100% de acerto" se constrói com humildade: o agente escala
   para um humano quando a decisão é irreversível, regulada ou fora do seu escopo.

## Os especialistas

### Engenharia
| Agente | Foco | Modelo mental |
|---|---|---|
| `arquiteto-software` | Arquitetura, design, trade-offs | Cultura de design da Amazon/Google |
| `engenheiro-cpp` | C++ moderno, performance, memória | Bjarne Stroustrup |
| `qa-testes` | Testes, qualidade, cobertura | Cultura de testes do Google |
| `seguranca-appsec` | AppSec, OWASP, vulnerabilidades | OWASP / práticas de Big Tech |
| `devops-sre` | CI/CD, build, confiabilidade | SRE do Google |
| `code-reviewer` | Revisão crítica de diffs | Engenharia de revisão do Google |

### Negócios
| Agente | Foco | Modelo mental |
|---|---|---|
| `estrategista-produto` | Visão de produto, descoberta | Marty Cagan / simplicidade da Apple |
| `growth-marketing` | Marketing, posicionamento, growth | Seth Godin / growth de SaaS |
| `vendas-receita` | Vendas, funil, receita | Metodologia consultiva (Salesforce) |
| `financeiro-fpa` | Finanças, FP&A, capital | Disciplina de valor de Warren Buffett |
| `juridico-compliance` | Jurídico, LGPD, contratos | Compliance corporativo |
| `dados-analytics` | Dados, métricas, decisão | Cultura data-driven da Netflix/Amazon |

### Orquestração
| Agente | Foco |
|---|---|
| `chefe-de-gabinete` | Decompõe demandas multi-área e coordena os especialistas |

> Nota de contexto: este repositório hoje é um **Jogo da Forca em C++** (projeto de
> aprendizado). Os agentes técnicos já são imediatamente úteis aqui. Os agentes de
> negócios estão prontos para quando o trabalho/empresa crescer — basta dar a eles o
> contexto real da empresa ao acioná-los.
