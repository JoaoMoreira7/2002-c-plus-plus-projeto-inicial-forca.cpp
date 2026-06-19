#!/usr/bin/env bash
# JM NFE — roda o extrator de liquidação com um comando só.
# 1ª vez: cria o ambiente e instala as dependências. Depois: só processa.
#
# Uso:
#   export ANTHROPIC_API_KEY="sua-chave"
#   ./rodar.sh meu_processo.pdf --planilha ../07-planilha-liquidacao-avancada.xlsx
#   ./rodar.sh ./pasta_de_processos --out ./saida        # modo lote
set -euo pipefail
cd "$(dirname "$0")"

VENV=".venv"

if [ ! -d "$VENV" ]; then
  echo ">> Primeira execução: criando ambiente e instalando dependências..."
  python3 -m venv "$VENV"
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
  pip install --quiet --upgrade pip
  pip install --quiet -r requirements.txt
else
  # shellcheck disable=SC1091
  source "$VENV/bin/activate"
fi

if [ -z "${ANTHROPIC_API_KEY:-}" ] && [ -z "${ANTHROPIC_AUTH_TOKEN:-}" ]; then
  echo "!! Defina sua chave antes de rodar:  export ANTHROPIC_API_KEY=\"sua-chave\"" >&2
  exit 1
fi

if [ "$#" -eq 0 ]; then
  echo "Uso: ./rodar.sh <PDF ou pasta> [--out DIR] [--planilha ARQ.xlsx] [--pdf-nativo]" >&2
  exit 1
fi

python extrator_liquidacao.py "$@"
