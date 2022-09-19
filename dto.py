from pydantic import BaseModel


class RatingDto(BaseModel):
    source_language: str
    target_language: str
    translation_id: str
    rating: int
