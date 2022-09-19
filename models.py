from sqlalchemy import Column, Integer, String

from database import Base


class RatingEntity(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    model_version = Column(String)
    translation_id = Column(String)
    rating = Column(Integer)
