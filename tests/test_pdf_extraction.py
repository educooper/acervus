from app.services.pdf_extraction_service import extract_sections_from_pdf

pdf_path = "uploads/meu_artigo.pdf"  # Caminho relativo do PDF
sections = extract_sections_from_pdf(pdf_path)

print("Título:", sections.get("title"))
print("Resumo:", sections.get("summary"))
print("Introdução:", sections.get("introduction"))
print("Referências:", sections.get("references"))
