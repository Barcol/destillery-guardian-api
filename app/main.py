from typing import List, Optional

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from app import models
from app.models import SessionLocal
from app import schemas

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(db: SessionLocal = Depends(get_db)) -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/sessions")
def read_sessions(db: SessionLocal = Depends(get_db)) -> List[models.Session]:
    sessions = db.query(models.Session).all()
    return sessions


@app.get("/sessions/{sess_id}")
def read_session(sess_id: str, db: SessionLocal = Depends(get_db)) -> models.Session:
    session = db.query(models.Session).filter_by(id=sess_id).one()
    return session


@app.get("/sessions/{sess_id}/results")
def get_results(sess_id: str, db: SessionLocal = Depends(get_db)) -> List[schemas.Result]:
    results = db.query(schemas.Result).filter_by(session_id=sess_id).all()
    return results


@app.get("/sessions/{sess_id}/results/{res_id}")
def get_result(res_id: str, sess_id: str, db: SessionLocal = Depends(get_db)) -> schemas.Result:
    result = db.query(schemas.Result).filter_by(id=res_id).all()
    return result


@app.post('/sessions/{sess_id}/results', response_model=schemas.Result)
async def create_result(sess_id: int, result: schemas.Result, db: SessionLocal = Depends(get_db)):
    result_to_database = models.Result(session_id=sess_id, temperature_1=result.temperature_1)
    db.add(result_to_database) # linijke wyżej mi coś nie leży xDDD chciałbym jednak przekazać całe Result naraz
    db.commit()
    return result.dict()
