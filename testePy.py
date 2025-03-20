import os
from docx import Document
import os
file_path = "Src/CertGarantia.docx"

if os.path.exists(file_path):
    doc = Document(file_path)
else:
    print(f"Arquivo não encontrado: {file_path}")