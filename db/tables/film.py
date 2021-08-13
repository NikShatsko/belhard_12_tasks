from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, autoincrement=True, primary_key=True)
    duration = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=False)
    rating = Column(Float, nullable=False)
    director_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)

    persons = relationship("Person")

    film_genres = relationship(
        "Genre",
        secondary="film_genres",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"Film id = {self.id}, film name = {self.name}"


