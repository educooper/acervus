import fitz  # PyMuPDF
import re

def extract_sections_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    # Limpa o texto e normaliza
    text = re.sub(r'\n+', '\n', text).strip()

    # Padrões para localizar seções
    patterns = {
        'resumo': r'(?:^|\n)(Resumo|RESUMO)(.*?)\n(?:Abstract|Introdução|INTRODUÇÃO|\n\n)',
        'introducao': r'(?:^|\n)(Introdução|INTRODUÇÃO)(.*?)\n(?:Referências|Bibliografia|\n\n)',
        'referencias': r'(?:^|\n)(Referências|REFERÊNCIAS|Bibliografia|BIBLIOGRAFIA)(.*?)$',
    }

    # Extrai seções com regex
    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            result[key] = match.group(2).strip()

    # Tenta pegar o título pelas primeiras linhas (antes do resumo geralmente)
    lines = text.split('\n')
    result['titulo'] = lines[0].strip() if lines else "Título não encontrado"

    return result
