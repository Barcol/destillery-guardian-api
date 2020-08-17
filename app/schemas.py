from datetime import datetime

from pydantic import BaseModel


class TerminationReason(BaseModel):
    termination_reason: str
    # "Sesja w trakcie!"
    # "Zatrzymany ręcznie z poziomu interfejsu graficznego"
    # "Zakończona z powodu przekroczenia temperatury"
    # "Zakończona z powodu przekroczenia wysokości cieszy"


class Session(BaseModel):
    name: str
    time_interval: int


class OutputSession(Session):
    id: int
    is_finished: bool
    distillation_date: datetime
    termination_reason: TerminationReason

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
