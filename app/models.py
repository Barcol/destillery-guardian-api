import datetime
import os

from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, Integer, Float, String, DateTime, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"), connect_args={})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def _get_date():
    return datetime.datetime.now()


class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, index=True)
    distillation_date = Column(Date, default=_get_date)
    name = Column(String)
    is_finished = Column(Boolean, default=False)
    time_interval = Column(Integer, default=30)
    result = relationship("Result")
    termination_reason = Column(String, default="Sesja w trakcie")

    def __repr__(self) -> str:
        return (f"<Session(id={self.id}, name={self.name}, distillation_date={self.distillation_date}, "
                f"is_finished={self.is_finished})>, termination_reason={self.termination_reason})>")


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=_get_date)
    session_id = Column(Integer, ForeignKey("session.id"))
    session = relationship("Session", back_populates="result")
    temperature_mash = Column(Float)
    temperature_steam = Column(Float)
    mass_obtained = Column(Integer)
    heating_power = Column(Integer)

    def __repr__(self) -> str:
        return (f"<Result(id={self.id}, session_id={self.session_id}, temperature_mash={self.temperature_mash})>, "
                f"temperature_steam={self.temperature_mash})>, mass_obtained={self.mass_obtained})>, "
                f"heating_power={self.heating_power})>")
