import fitz
from pathlib import Path

NEW_FONT_SIZE = 12  
# NEW_FONT_NAME = "TiRo"  #descomenta para cambiar la fuente

input_dir = Path.cwd()
# Directorio de salida para PDFs modificados
output_dir = input_dir / "modified_pdfs"
output_dir.mkdir(exist_ok=True)

for pdf_file in input_dir.glob("*.pdf"):
    doc = fitz.open(pdf_file)
    for page in doc:
        for widget in page.widgets(): 
            # Omitir campos de firma
            if widget.field_type_string == "Signature":
                continue

            if hasattr(widget, "text_fontsize"):
                widget.text_fontsize = NEW_FONT_SIZE
                # widget.text_font = NEW_FONT_NAME  #descomenta para cambiar la fuente
                widget.update()

    out_file = output_dir / f"{pdf_file.stem}_modified.pdf"
    doc.save(out_file)
    doc.close()
    print(f"Procesado: {pdf_file.name} -> {out_file.name}")
