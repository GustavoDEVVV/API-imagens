from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

app = FastAPI()

# Diretório onde os arquivos serão armazenados
UPLOAD_FOLDER = "static/files"
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

# Servindo a pasta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Página HTML para upload
@app.get("/", response_class=HTMLResponse)
def upload_form():
    return open("index.html").read()

# Upload de arquivo
@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb+") as f:
        f.write(await file.read())
    return RedirectResponse(url=f"/static/files/{file.filename}", status_code=302)
