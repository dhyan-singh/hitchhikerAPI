from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

from random import randint
import asyncio

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def read_file(path: str):
    with open(f'static/{path}') as f:
        return f.read()


@app.get("/", response_class=HTMLResponse)
async def home():
    tasks = [read_file('home.html')]
    result = await asyncio.gather(*tasks)
    return result[0]


def random_quote(db: Session):
    random = randint(0, 100)
    return crud.get_quotes(db)


@app.put("/add_quote", response_model=schemas.Quote)
def add_quote(quote: schemas.CreateQuote, db: Session = Depends(get_db)):
    try:
        quote = crud.add_quote(db, quote=quote)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Quote already exists")
    except ValueError as e:
        raise HTTPException(status_code=409, detail=e.args[0])
    return quote


@app.put("/add_character", response_model=schemas.Character)
def add_character(character: schemas.CreateCharacter, db: Session = Depends(get_db)):
    try:
        char = crud.add_character(db, character=character)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Character Already Exists")
    return char


@app.get("/quote", response_model=list[schemas.Quote])
def quote(id: int | None = None, db: Session = Depends(get_db)):
    if not id:
        quote = random_quote(db)
    quote = crud.get_quote(db, id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Quote with id not found")
    return [quote]


@app.get("/quotes", response_model=list[schemas.Quote])
def quotes(db: Session = Depends(get_db)):
    return crud.get_quotes(db)


@app.get("/characters", response_model=list[schemas.Character])
def get_characters(db: Session = Depends(get_db)):
    return crud.get_characters(db)
