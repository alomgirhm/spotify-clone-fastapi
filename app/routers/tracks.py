from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas import TrackModel, TrackUpdateModel, Track, TrackCreate
from app.dependencies import get_db
from app.crud.tracks_crud import (
    create_track,
    get_all_tracks,
    get_track,
    delete_track,
    update_track
)

tracks_router = APIRouter()

# bug 1 fix — database থেকে আনো
@tracks_router.get("/tracks/", response_model=List[TrackModel])
def get_tracks(db: Session = Depends(get_db)):
    return get_all_tracks(db=db)

# এইটা আগে থেকেই ঠিক ছিলো
@tracks_router.post("/tracks", response_model=Track)
def create_track_route(track_dto: TrackCreate, db: Session = Depends(get_db)):
    return create_track(db=db, track_dto=track_dto)

# bug 2, 4, 5 fix — database থেকে আনো, নাম change করো
@tracks_router.get("/tracks/{track_id}", response_model=TrackModel)
def get_single_track(track_id: int, db: Session = Depends(get_db)):
    db_track = get_track(db=db, track_id=track_id)
    if db_track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Track not found"
        )
    return db_track

# bug 3, 5 fix — database থেকে delete করো
@tracks_router.delete("/tracks/{track_id}")
def delete_track_route(track_id: int, db: Session = Depends(get_db)):
    result = delete_track(db=db, track_id=track_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Track not found"
        )
    return {"message": "Track deleted successfully"}

# bug 4 fix — নাম change করো
@tracks_router.put("/tracks/{track_id}", response_model=TrackModel)
def update_track_route(track_id: int, track_dto: TrackUpdateModel, db: Session = Depends(get_db)):
    db_track = update_track(db=db, track_id=track_id, track_dto=track_dto)
    if db_track is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Track not found"
        )
    return db_track