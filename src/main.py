from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from random import randint
import asyncio

app = FastAPI()

quotes = {
    0: "Don't Panic",
    1: "Life is Fun",
    2: "Something, Something, Something",
}


async def read_file(path: str):
    with open(f'static/{path}') as f:
        return f.read()


@app.get("/", response_class=HTMLResponse)
async def home():
    tasks = [read_file('home.html')]
    result = await asyncio.gather(*tasks)
    return result[0]


def random_quote():
    random = randint(0, 100)
    return quotes[random]


@app.get("/quote")
def quote(id: int | None = None):
    if not id:
        quote = random_quote()
    return {"quote": quotes[id]}
