from fastapi import FastAPI, Depends

from app import models
from app.models import SessionLocal

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(db: SessionLocal = Depends(get_db)):
    return {"Hello": "World"}


@app.get("/sessions")
def read_sessions(db: SessionLocal = Depends(get_db)):
    sessions = db.query(models.Session).all()
    return sessions


@app.get("/session/{sess_id}")
def read_session(sess_id, db: SessionLocal = Depends(get_db)):
    session = db.query(models.Session).filter_by(id=sess_id).one()
    return session


@app.get("/session/{sess_id}/results")
def get_result(sess_id, db: SessionLocal = Depends(get_db)):
    results = db.query(models.Result).filter_by(session_id=sess_id).all()
    return results


@app.get("/result/{res_id}")
def get_results(res_id, db: SessionLocal = Depends(get_db)):
    result = db.query(models.Result).filter_by(id=res_id).all()
    return result
