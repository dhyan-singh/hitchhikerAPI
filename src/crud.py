from sqlalchemy.orm import Session

from . import models, schemas


def add_quote(db: Session, quote: schemas.CreateQuote):
    character = db.query(models.Character).get(quote.character_id)
    if character:
        db_quote = models.Quote(
            quote=quote.quote, character_id=quote.character_id)
        db.add(db_quote)
        db.commit()
        db.refresh(db_quote)
        return db_quote
    else:
        raise ValueError(
            f"Character with id '{quote.character_id}' doesn't exist")


def add_character(db: Session, character: schemas.CreateCharacter):
    db_character = models.Character(name=character.name)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


def get_quotes_by_character_id(db: Session, character_id: int):
    return db.query(models.Quote).filter(models.Quote.character_id == character_id).all()


def get_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()


def get_quotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quote).offset(skip).limit(limit).all()


def get_quote(db: Session, id: int):
    return db.query(models.Quote).filter(models.Quote.id == id).first()


def get_character_by_id(db: Session, id: int = 0):
    return db.query(models.Character).filter(models.Character.id == id).first()
