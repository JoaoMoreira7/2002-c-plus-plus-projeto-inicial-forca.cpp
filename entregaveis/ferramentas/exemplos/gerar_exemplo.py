#!/usr/bin/env python3
"""Gera um PDF de SENTENÇA FICTÍCIA para testar o extrator.
Todos os dados são inventados (nomes, processo, empresa) — não é caso real.
Requer reportlab:  pip install reportlab
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

SAIDA = Path(__file__).parent / "sentenca_exemplo.pdf"

TEXTO = [
    ("titulo", "PODER JUDICIÁRIO — JUSTIÇA DO TRABALHO"),
    ("titulo", "TRIBUNAL REGIONAL DO TRABALHO DA 2ª REGIÃO — 1ª Vara do Trabalho de São Paulo"),
    ("sub", "SENTENÇA (DOCUMENTO FICTÍCIO PARA TESTE — DADOS INVENTADOS)"),
    ("p", "Processo nº 0001234-56.2023.5.02.0001"),
    ("p", "Reclamante: JOÃO DA SILVA EXEMPLO"),
    ("p", "Reclamada: EMPRESA MODELO COMÉRCIO LTDA."),
    ("p", "Data do ajuizamento da ação: 10/01/2023."),
    ("h", "I — RELATÓRIO"),
    ("p", "Trata-se de reclamação trabalhista em que o reclamante, admitido em "
          "01/02/2020 na função de auxiliar administrativo, com último salário-base de "
          "R$ 2.000,00 (dois mil reais), foi dispensado sem justa causa em 30/06/2024. "
          "A jornada contratual era de 44 horas semanais."),
    ("h", "II — FUNDAMENTAÇÃO"),
    ("p", "Restou comprovada a prestação habitual de horas extras não quitadas, bem como "
          "diferenças salariais decorrentes de desvio de função no período indicado."),
    ("h", "III — DISPOSITIVO"),
    ("p", "Ante o exposto, julgo PROCEDENTES EM PARTE os pedidos para condenar a reclamada "
          "ao pagamento das seguintes verbas:"),
    ("p", "a) Horas extras a 50%, com adicional convencional, referentes ao período de "
          "01/02/2021 a 30/06/2023, com reflexos em DSR, 13º salário, férias acrescidas de "
          "1/3 e FGTS;"),
    ("p", "b) Diferenças salariais por desvio de função no período de 01/03/2020 a "
          "31/12/2022, com reflexos nas demais verbas;"),
    ("p", "c) Verbas rescisórias: saldo de salário, aviso prévio indenizado, 13º salário "
          "proporcional e férias proporcionais acrescidas de 1/3;"),
    ("p", "d) Multa do art. 477, § 8º, da CLT;"),
    ("p", "e) FGTS do período contratual não recolhido, acrescido da multa de 40%."),
    ("p", "A correção monetária e os juros de mora observarão os critérios fixados pelo "
          "C. STF na ADC 58, conforme se apurar em liquidação, respeitada a fase processual."),
    ("p", "Liquidação por cálculos. Custas pela reclamada."),
    ("p", "São Paulo, 15 de agosto de 2024. (assinatura — documento fictício)"),
]


def gerar(saida: Path = SAIDA) -> Path:
    styles = getSampleStyleSheet()
    estilos = {
        "titulo": ParagraphStyle("t", parent=styles["Title"], fontSize=12, leading=15, spaceAfter=4),
        "sub": ParagraphStyle("s", parent=styles["Heading3"], textColor="#666666", spaceAfter=10),
        "h": ParagraphStyle("h", parent=styles["Heading2"], fontSize=11, spaceBefore=8, spaceAfter=4),
        "p": ParagraphStyle("p", parent=styles["BodyText"], fontSize=10.5, leading=15,
                            alignment=4, spaceAfter=6),
    }
    doc = SimpleDocTemplate(str(saida), pagesize=A4,
                            leftMargin=2.5 * cm, rightMargin=2.5 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm,
                            title="Sentença (exemplo fictício)")
    flow = []
    for tipo, txt in TEXTO:
        flow.append(Paragraph(txt, estilos[tipo]))
        if tipo in ("titulo", "sub"):
            flow.append(Spacer(1, 2))
    doc.build(flow)
    return saida


if __name__ == "__main__":
    caminho = gerar()
    print(f"PDF de exemplo gerado: {caminho}")
