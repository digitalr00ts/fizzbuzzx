from fastapi import FastAPI
from fizzbuzz import fizzbuzz

app = FastAPI()


@app.get("/fizzbuzzx/")
async def root(number: int = 6):
    return {"message": fizzbuzz(number)}
