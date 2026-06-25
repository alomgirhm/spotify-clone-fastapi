from sqlalchemy import Column, String, Integer, DATE, TIME
from .database import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    release_date = Column(DATE, nullable=False)
    duration = Column(TIME, nullable=False)