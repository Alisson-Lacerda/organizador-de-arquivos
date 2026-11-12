import os, shutil

pasta = os.path.expanduser("~/Downloads")
gavetas = {".jpg": "Imagens", ".jpeg": "Imagens", ".png": "Imagens", ".pdf": "PDFs", ".exe": "Executáveis", ".zip": "Compactados", ".docx": "Documentos", ".webp": "Imagens", ".csv": "Planilhas", ".xlsx": "Planilhas"}

def organizar_downloads():
    for nome in os.listdir(pasta):
        ext = os.path.splitext(nome)[1].lower()
        if ext in gavetas:
            destino = os.path.join(pasta, gavetas[ext])
            os.makedirs(destino, exist_ok=True)
            shutil.move(os.path.join(pasta, nome), destino)
organizar_downloads()