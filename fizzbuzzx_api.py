from fastapi import FastAPI
from fizzbuzz import fizzbuzz

app = FastAPI()


@app.get("/")
async def root(value: int = 0):
    return {"message": fizzbuzz(value)}
