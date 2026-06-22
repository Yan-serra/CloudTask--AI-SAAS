from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "CloudTask AI SaaS"}
