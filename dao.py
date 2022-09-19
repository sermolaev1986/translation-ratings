from sqlalchemy.orm import Session
from models import RatingEntity


class RatingDao:
    def save_rating(self, rating: RatingEntity, db: Session) -> RatingEntity:
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return rating
