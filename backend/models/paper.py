from pydantic import BaseModel

class Paper(BaseModel):

    title: str

    abstract: str | None = None

    year: int | None = None

    url: str | None = None