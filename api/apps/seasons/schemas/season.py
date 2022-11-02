from pydantic import BaseModel

from api.apps.films.schemas import FilmResponse


class SeasonBase(BaseModel):
    number: int


class SeasonRequest(SeasonBase):
    series_id: int


class SeasonResponse(SeasonBase):
    id: int
    series: FilmResponse

    class Config:
        orm_mode = True
