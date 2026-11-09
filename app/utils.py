import io
import pypdf

def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    """Extract raw text from PDF byte content."""
    pdf_reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
    extracted_text = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text.append(text)
    return "\n".join(extracted_text)