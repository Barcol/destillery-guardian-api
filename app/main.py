from typing import List, Optional

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from app import schemas
from app.schemas import SessionLocal
from app import models

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
def read_sessions(db: SessionLocal = Depends(get_db)) -> List[schemas.Session]:
    sessions = db.query(schemas.Session).all()
    return sessions


@app.get("/sessions/{sess_id}")
def read_session(sess_id: str, db: SessionLocal = Depends(get_db)) -> schemas.Session:
    session = db.query(schemas.Session).filter_by(id=sess_id).one()
    return session


@app.get("/sessions/{sess_id}/results")
def get_results(sess_id: str, db: SessionLocal = Depends(get_db)) -> List[schemas.Result]:
    results = db.query(schemas.Result).filter_by(session_id=sess_id).all()
    return results


@app.get("/sessions/{sess_id}/results/{res_id}")
def get_result(res_id: str, sess_id: str, db: SessionLocal = Depends(get_db)) -> schemas.Result:
    result = db.query(schemas.Result).filter_by(id=res_id).all()
    return result


@app.post('/sessions/{sess_id}/results', response_model=models.Result)
async def create_result(sess_id: int, result: models.Result, db: SessionLocal = Depends(get_db)):
    return result.dict()
