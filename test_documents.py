from app.config import DOCUMENTS_DIR

files = sorted(DOCUMENTS_DIR.glob("*"))

print(f"\nTotal Files : {len(files)}\n")

for i, file in enumerate(files, start=1):
    print(f"{i}. {file.name}")