from pydantic import BaseModel


class Session(BaseModel):
    name: str
    is_finished: bool


class OutputSession(Session):
    id: int


class Result(BaseModel):
    temperature_1: int


class OutputResult(Result):
    id: int
    session_id: int

    class Config:
        orm_mode = True
