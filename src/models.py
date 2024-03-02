from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    quotes = relationship("Quote", back_populates="characters")


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    quote = Column(String)

    character_id = Column(Integer, ForeignKey("characters.id"))

    characters = relationship("Character", back_populates="quotes")
