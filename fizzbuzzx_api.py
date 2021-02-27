"""
API framework for fizzbuzzx
"""
from typing import Dict

from fastapi import FastAPI
from fizzbuzzx import fizzbuzz

app = FastAPI()


@app.get("/fizzbuzzx/")
async def root(number: int = 6) -> Dict:
    """Path operation function for fizzbuzzx

    Args:
        number (int): integer to generate numbers up to

    Returns:
        JSON payload of generated numbers
    """
    return {"message": fizzbuzz(number)}
