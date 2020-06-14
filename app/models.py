import os

from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"), connect_args={})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_finished = Column(Boolean, default=True)
    result = relationship("Result")


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("session.id"))
    session = relationship("Session", back_populates="result")
    temperature_1 = Column(Integer)

    def __repr__(self) -> str:
        return f"<Result(session_id={self.session_id})>"
