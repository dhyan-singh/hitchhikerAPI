from fastapi import FastAPI
from random import randint
app = FastAPI()

quotes = {
    0: "Don't Panic",
    1: "Life is Fun",
    2: "Something, Something, Something",
}

instructions = '''
Get quotes from Hitchhiker's Guide To The Galaxy
'''

@app.get("/")
def home():
    return instructions.strip()

def random_quote():
    random = randint(0, 100)
    return quotes[random]

@app.get("/quote")
def quote(id: int | None = None):
    if not id:
        quote = random_quote()
    return {"quote": quotes[id]}