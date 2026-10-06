from fastapi import FastAPI
from src.utils.db import Base,engine


Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/home")
def home():
    return {"message": "Hello World"}