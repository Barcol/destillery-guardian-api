from typing import List

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from app import schemas
from app.schemas import SessionLocal

from app.models import Result

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


@app.get("/session/{sess_id}")
def read_session(sess_id: str, db: SessionLocal = Depends(get_db)) -> schemas.Session:
    session = db.query(schemas.Session).filter_by(id=sess_id).one()
    return session


@app.get("/session/{sess_id}/results")
def get_result(sess_id: str, db: SessionLocal = Depends(get_db)) -> List[schemas.Result]:
    results = db.query(schemas.Result).filter_by(session_id=sess_id).all()
    return results


@app.get("/result/{res_id}")
def get_results(res_id: str, db: SessionLocal = Depends(get_db)) -> schemas.Result:
    result = db.query(schemas.Result).filter_by(id=res_id).all()
    return result


@app.post('/results/')
async def create_result(result: Result = None, db: SessionLocal = Depends(get_db), response_model=Result):
    return result.dict()
