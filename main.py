from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from dto import RatingDto
from model_version_service import ModelVersionService
from rating_service import RatingService

app = FastAPI()
model_version_service = ModelVersionService()
rating_service = RatingService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ratings")
async def post_rating(rating: RatingDto, db: Session = Depends(get_db)):
    model_version = model_version_service.get_model_version(rating.source_language, rating.target_language)
    return rating_service.save_rating(rating, model_version, db)
