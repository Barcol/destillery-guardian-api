from pydantic import BaseModel
from datetime import datetime


class Session(BaseModel):
    name: str


class OutputSession(Session):
    id: int
    is_finished: bool
    distillation_date: datetime

    class Config:
        orm_mode = True


class Result(BaseModel):
    temperature_1: int


class OutputResult(Result):
    id: int
    created_at: datetime
    session_id: int

    class Config:
        orm_mode = True
