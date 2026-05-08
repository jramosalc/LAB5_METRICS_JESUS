from fastapi import FastAPI, UploadFile
import shutil
import os
from lab5_metrics.services.metrics_service import analizar

app = FastAPI(title="API de Jesus Ramos")

@app.post("/analyze-metrics")
def analyze(file: UploadFile):
    os.makedirs("data", exist_ok=True)
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return analizar(path)