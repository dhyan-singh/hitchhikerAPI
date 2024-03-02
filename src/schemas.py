from pydantic import BaseModel


class Quote(BaseModel):
    id: int
    quote: str
    character_id: int

    class Config:
        from_attributes = True


class Character(BaseModel):
    id: int
    name: str
    quotes: list[Quote]

    class Config:
        from_attributes = True


class CreateCharacter(BaseModel):
    name: str
    quotes: list[Quote] | None = None

    class Config:
        from_attributes = True


class CreateQuote(BaseModel):
    quote: str
    character_id: int

    class Config:
        from_attributes = True
