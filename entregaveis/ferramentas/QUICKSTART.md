# Início rápido — fluxo do perito (JM NFE)

O objetivo: você joga o **PDF do processo** e recebe um **relatório de conferência** +
a **planilha de liquidação pré-preenchida**. Você confere, lança os valores e fecha o laudo.

## Uma vez só (configuração)
1. Instale o Python 3 (se ainda não tiver).
2. Pegue sua chave da Claude API e exporte:
   ```bash
   export ANTHROPIC_API_KEY="sua-chave"
   ```
   (No Windows: use o WSL/Git Bash, ou rode os comandos `python` direto — ver README.)

## No dia a dia
```bash
# Um processo:
./rodar.sh caso_fulano.pdf --planilha ../07-planilha-liquidacao-avancada.xlsx

# Vários de uma vez (uma pasta cheia de PDFs):
./rodar.sh ./processos_do_mes --out ./saida --planilha ../07-planilha-liquidacao-avancada.xlsx
```

Saídas geradas:
- `*_relatorio.md` — **comece por aqui**: dados extraídos + trechos-fonte + checklist do que revisar.
- `*_extracao.json` — os dados em formato estruturado.
- `*_liquidacao_preenchida.xlsx` — cópia da planilha 07 com as **verbas** e a **memória** já lançadas.

## Os 5 passos da perícia (do PDF ao laudo)
1. **Rodar** o extrator no PDF → abrir o `*_relatorio.md`.
2. **Conferir** cada campo no documento (a IA propõe, você decide).
3. **Lançar** os valores históricos por competência na aba `Verbas` da planilha.
4. **Preencher** a aba `Indices` com a tabela oficial do TRT/CSJT do período
   (ver `../06-tabelas-indices-2026-e-metodologia.md`) → a correção sai por competência.
5. **Reconferir** o total por método independente e gerar o laudo (`../03-modelo-laudo-pericial.md`).

> Veja `exemplos/saida_demonstracao.md` para um exemplo de relatório (sentença fictícia).
> Lembrete: ferramenta de apoio. A responsabilidade técnica é do perito.
