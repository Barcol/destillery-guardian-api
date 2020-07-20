from pydantic import BaseModel
from datetime import datetime


class Session(BaseModel):
    name: str
    time_interval: int


class OutputSession(Session):
    id: int
    is_finished: bool
    distillation_date: datetime

    class Config:
        orm_mode = True


class Result(BaseModel):
    temperature_mash: float
    temperature_steam: float
    mass_obtained: int
    heating_power: int


class OutputResult(Result):
    id: int
    created_at: datetime
    session_id: int

    class Config:
        orm_mode = True
