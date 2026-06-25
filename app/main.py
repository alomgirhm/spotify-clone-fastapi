from fastapi import FastAPI 
from .routers import tracks_router
from .database import engine
from .models import Base



Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(tracks_router)
