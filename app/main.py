from fastapi import FastAPI, UploadFile
import shutil
from ocr import run_ocr
from parser import extract_fields

app = FastAPI()

@app.post("/ocr")
async def ocr_api(file: UploadFile):
    path = f"/tmp/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    texts = run_ocr(path)
    fields = extract_fields(texts)

    return {
        "raw_text": texts,
        "fields": fields
    }
