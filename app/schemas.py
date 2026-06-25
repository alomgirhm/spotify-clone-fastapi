from pydantic import BaseModel
from datetime import date, time

class TrackBase(BaseModel):
   
    title: str
    release_date: date | None = None
    duration: time | None = None

class TrackCreate(TrackBase):
    pass

class Track(TrackBase):
    id: int

    class Config:
        form_attributes = True
    

class TrackModel(BaseModel):
    id:int
    title:str

class TrackUpdateModel(BaseModel):
    title:str

