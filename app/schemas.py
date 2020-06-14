from pydantic import BaseModel


class Result(BaseModel):
    session: int
    temperature_1: int
