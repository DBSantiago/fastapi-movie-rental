from pydantic import BaseModel, validator

from api.apps.seasons.schemas.season import SeasonResponse
from api.utils.validation.data_validation import DataValidation


class EpisodeBase(BaseModel):
    title: str
    number: int

    @validator('title')
    def field_not_empty(cls, value):
        return DataValidation.field_not_empty(value)


class EpisodeRequest(EpisodeBase):
    season_id: int


class EpisodeResponse(EpisodeBase):
    id: int
    season: SeasonResponse

    class Config:
        orm_mode = True
