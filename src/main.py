from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from random import randint


app = FastAPI()

quotes = {
    0: "Don't Panic",
    1: "Life is Fun",
    2: "Something, Something, Something",
}

instructions = '''
<h1>
Get quotes from Hitchhiker's Guide To The Galaxy
</h1>

For API Documentation - <a href="/docs/"> Swagger Docs </a>
'''


@app.get("/", response_class=HTMLResponse)
def home():
    return instructions


def random_quote():
    random = randint(0, 100)
    return quotes[random]


@app.get("/quote")
def quote(id: int | None = None):
    if not id:
        quote = random_quote()
    return {"quote": quotes[id]}
