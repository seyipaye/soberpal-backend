from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Examples(BaseModel):
    id: str | None
    name: str
    active: bool

    class Config:
        orm_mode = True


class ExampleSchema(Examples):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Day(BaseModel):
    # day_id: str | None = Field(
    #     title="The date of the day in YYYY-MM-DD format", example='2022-01-31'
    # )
    date: str
    bottles: int

    class Config:
        orm_mode = True


class Ranking(BaseModel):
    id: int
    clean_days: int

    class Config:
        orm_mode = True


class Months(BaseModel):
    title: str
    bottle_count: int

    class Config:
        orm_mode = True


class GetAllHistoryResult(BaseModel):
    status_code: int
    result: list[Months]
