from fastapi import FastAPI
from pydantic import BaseModel
from chat import ask_question
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

app = FastAPI()

class Question(BaseModel):
    question:str

@app.post("/ask")

def ask(q:Question):

    answer=ask_question(
        q.question
    )

    return {
        "answer":answer
    }

templates = Jinja2Templates(directory="templates")
print(os.getcwd())
print(os.listdir("templates"))

@app.get("/", response_class=HTMLResponse)
def home(request:Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )