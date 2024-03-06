import spacy
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import shutil
import os

app = FastAPI()

nlp = spacy.load("en_core_web_sm") 

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "static/index.html"

@app.post("/upload")
async def update_resume(resume: UploadFile = )