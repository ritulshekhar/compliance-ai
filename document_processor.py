import io
import PyPDF2
import pdfplumber
import docx
from typing import Optional, Dict, Any

class DocumentProcessor:
    def __init__(self):
        pass

    def extract_text(self, file_obj: io.BytesIO, file_type: str) -> str:
        """Extracts text from various file formats."""
        file_type = file_type.lower()
        text = ""

        try:
            if file_type == 'pdf':
                text = self._extract_from_pdf(file_obj)
            elif file_type == 'docx':
                text = self._extract_from_docx(file_obj)
            elif file_type == 'txt':
                text = str(file_obj.read(), "utf-8")
            else:
                raise ValueError(f"Unsupported file type: {file_type}")
        except Exception as e:
            return f"Error extracting text: {str(e)}"

        return text

    def _extract_from_pdf(self, file_obj: io.BytesIO) -> str:
        text = ""
        # Try pdfplumber first for better extraction
        try:
            with pdfplumber.open(file_obj) as pdf:
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
        except Exception:
            # Fallback to PyPDF2
            file_obj.seek(0)
            reader = PyPDF2.PdfReader(file_obj)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        return text

    def _extract_from_docx(self, file_obj: io.BytesIO) -> str:
        doc = docx.Document(file_obj)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text

    def get_document_metadata(self, file_obj: io.BytesIO, file_type: str) -> Dict[str, Any]:
        """Extracts metadata from the document."""
        meta = {"file_type": file_type, "size_bytes": file_obj.getbuffer().nbytes}
        return meta
