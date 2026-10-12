from PyPDF2 import PdfReader
import sys

try:
    path = 'OmnitronTech Redesign Proposal.pdf'
    reader = PdfReader(path)
    out_path = 'OmnitronTech_Redesign_Proposal.txt'
    with open(out_path, 'w', encoding='utf-8') as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            f.write(f'=== PAGE {i+1} ===\n')
            if text:
                f.write(text)
            else:
                f.write('[No extractable text]\n')
            f.write('\n\n')
    print(f'DONE: {len(reader.pages)} pages written to {out_path}')
    sys.exit(0)
except Exception as e:
    print('ERR', e)
    sys.exit(1)
