from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
import uvicorn

app = FastAPI()


class Sentence(BaseModel):
    sentence: str


@app.post("/analyze/")
def analyze(SentenceReference: Sentence):
    blob = TextBlob(SentenceReference.sentence)
    return blob.sentiment


@app.get("/")
def intro():
    return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
