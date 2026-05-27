import fitz
import sys
import os

path = sys.argv[1]
out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(path)[0] + '.txt'

doc = fitz.open(path)
with open(out_path, 'w', encoding='utf-8') as f:
    for page in doc:
        f.write(page.get_text())
doc.close()
print(f"Extracted to: {out_path}")
