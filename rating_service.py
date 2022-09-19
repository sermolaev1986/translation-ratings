from sqlalchemy.orm import Session

from dao import RatingDao
from dto import RatingDto
from models import RatingEntity

rating_dao = RatingDao()


class RatingService:
    def save_rating(self, rating: RatingDto, model_version: str, db: Session) -> RatingDto:
        rating_dao.save_rating(RatingEntity(
            model_version=model_version,
            translation_id=rating.translation_id,
            rating=rating.rating), db=db)
        return rating
