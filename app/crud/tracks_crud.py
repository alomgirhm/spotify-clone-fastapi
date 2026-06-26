from sqlalchemy.orm import Session
from app.schemas import TrackCreate
from app.models import Track

def create_track(db: Session, track_dto: TrackCreate):
    db_track = Track(
        title=track_dto.title,
        duration=track_dto.duration,
        release_date=track_dto.release_date
    )
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

# নতুন function — সব গান আনো
def get_all_tracks(db: Session):
    return db.query(Track).all()

# নতুন function — একটা গান আনো
def get_track(db: Session, track_id: int):
    return db.query(Track).filter(Track.id == track_id).first()

# নতুন function — গান delete করো
def delete_track(db: Session, track_id: int):
    db_track = db.query(Track).filter(Track.id == track_id).first()
    if db_track:
        db.delete(db_track)
        db.commit()
        return True
    return False

# নতুন function — গান update করো
def update_track(db: Session, track_id: int, track_dto):
    db_track = db.query(Track).filter(Track.id == track_id).first()
    if db_track:
        db_track.title = track_dto.title
        db.commit()
        db.refresh(db_track)
        return db_track
    return None