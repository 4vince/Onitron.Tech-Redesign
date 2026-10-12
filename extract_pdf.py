from PyPDF2 import PdfReader
import sys

try:
    path = 'OmnitronTech Redesign Proposal.pdf'
    reader = PdfReader(path)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            print(f"=== PAGE {i+1} ===")
            print(text)
            print()
    sys.exit(0)
except Exception as e:
    print('ERR', e)
    sys.exit(1)
