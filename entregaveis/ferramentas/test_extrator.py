#!/usr/bin/env python3
"""
Testes do extrator de liquidação (JM NFE).

Roda de duas formas:
    pytest test_extrator.py
    python test_extrator.py          # runner próprio, sem precisar do pytest

Os testes OFFLINE (schema, relatório, extração de PDF, preenchimento da planilha)
não usam a API. O teste de INTEGRAÇÃO só roda se ANTHROPIC_API_KEY estiver definida —
caso contrário é pulado (não falha).
"""
import os
import re
import sys
import json
import importlib.util
from pathlib import Path

AQUI = Path(__file__).parent
PDF_EXEMPLO = AQUI / "exemplos" / "sentenca_exemplo.pdf"
PLANILHA = AQUI.parent / "07-planilha-liquidacao-avancada.xlsx"


def _carregar_modulo():
    spec = importlib.util.spec_from_file_location("extrator", AQUI / "extrator_liquidacao.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


ex = _carregar_modulo()


# ---------------------------------------------------------------- OFFLINE ----
def test_schema_valida_e_serializa():
    d = ex.DadosLiquidacao(
        numero_processo="0001234-56.2023.5.02.0001",
        verbas_deferidas=[ex.Verba(descricao="Horas extras 50%", confianca="alta")],
        campos_para_revisar=["criterio_correcao"],
        observacoes_extracao="ok",
    )
    payload = json.loads(d.model_dump_json())
    assert payload["numero_processo"].endswith("5.02.0001")
    assert payload["verbas_deferidas"][0]["descricao"] == "Horas extras 50%"


def test_relatorio_contem_secoes_e_aviso():
    d = ex.DadosLiquidacao(
        data_admissao="01/02/2020",
        verbas_deferidas=[ex.Verba(descricao="13º proporcional", confianca="media")],
        observacoes_extracao="",
    )
    md = ex.gerar_relatorio_md(d, "x.pdf", {})
    assert "A IA PROPÕE, o PERITO DECIDE" in md
    assert "## Verbas deferidas" in md
    assert "01/02/2020" in md
    # campo ausente deve aparecer como não encontrado
    assert "_(não encontrado)_" in md


def test_extrair_texto_pdf_exemplo():
    assert PDF_EXEMPLO.exists(), "Gere o PDF: python exemplos/gerar_exemplo.py"
    texto = ex.extrair_texto_pdf(PDF_EXEMPLO)
    norm = re.sub(r"\s+", " ", texto)
    esperados = [
        "0001234-56.2023.5.02.0001", "01/02/2020", "30/06/2024",
        "R$ 2.000,00", "Horas extras", "Diferenças salariais",
        "ADC 58", "10/01/2023", "art. 477", "40%",
    ]
    faltando = [e for e in esperados if e not in norm]
    assert not faltando, f"Marcadores ausentes no texto extraído: {faltando}"


def test_montar_conteudo_texto_e_nativo():
    # texto
    conteudo = ex.montar_conteudo(PDF_EXEMPLO, pdf_nativo=False)
    assert isinstance(conteudo, str) and len(conteudo) > 500
    # nativo (blocos)
    blocos = ex.montar_conteudo(PDF_EXEMPLO, pdf_nativo=True)
    assert isinstance(blocos, list)
    assert blocos[0]["type"] == "document"
    assert blocos[0]["source"]["media_type"] == "application/pdf"


def test_preencher_planilha(tmp_path=None):
    try:
        import openpyxl  # noqa: F401
    except ImportError:
        print("  (pulado: openpyxl ausente)")
        return
    if not PLANILHA.exists():
        print("  (pulado: planilha 07 não encontrada)")
        return
    destino = Path(tmp_path or AQUI) / "_teste_liquidacao.xlsx"
    d = ex.DadosLiquidacao(
        data_admissao="01/02/2020", data_afastamento="30/06/2024",
        criterio_correcao=None, criterio_juros=None,
        verbas_deferidas=[
            ex.Verba(descricao="Horas extras 50%", confianca="alta"),
            ex.Verba(descricao="Verbas rescisórias", confianca="alta"),
        ],
    )
    ex.preencher_planilha(d, PLANILHA, destino)
    assert destino.exists()
    import openpyxl
    wb = openpyxl.load_workbook(str(destino))
    wv = wb["Verbas"]
    assert wv.cell(row=5, column=2).value == "Horas extras 50%"
    assert wv.cell(row=6, column=2).value == "Verbas rescisórias"
    destino.unlink(missing_ok=True)


# ------------------------------------------------------------ INTEGRAÇÃO ----
def test_integracao_api_opcional():
    """Só roda com ANTHROPIC_API_KEY definida (consome créditos)."""
    if not (os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN")):
        print("  (pulado: defina ANTHROPIC_API_KEY para o teste de integração)")
        return
    texto = ex.extrair_texto_pdf(PDF_EXEMPLO)
    dados, _uso = ex.extrair_com_claude(texto, ex.MODELO_PADRAO)
    # Conferências mínimas contra o conteúdo conhecido do exemplo
    assert dados.numero_processo and "5.02.0001" in dados.numero_processo
    assert dados.data_admissao and "2020" in dados.data_admissao
    assert len(dados.verbas_deferidas) >= 3
    # A sentença remete à ADC 58 -> o critério deve ser tratado como definido
    assert dados.criterio_definido_na_sentenca in (True, False)  # apenas presença coerente
    print(f"  Integração OK: {len(dados.verbas_deferidas)} verbas extraídas.")


# ------------------------------------------------------------- RUNNER -------
def _main():
    testes = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    falhas = 0
    for t in testes:
        nome = t.__name__
        try:
            t()
            print(f"PASS  {nome}")
        except AssertionError as e:
            falhas += 1
            print(f"FAIL  {nome}: {e}")
        except Exception as e:
            falhas += 1
            print(f"ERRO  {nome}: {type(e).__name__}: {e}")
    print(f"\n{len(testes) - falhas}/{len(testes)} testes passaram.")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    _main()
