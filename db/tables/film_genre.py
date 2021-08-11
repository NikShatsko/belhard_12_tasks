from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class FilmGenre(Base):
    __tablename__ = "film_genres"

    film_id = Column(Integer, ForeignKey("films.id", ondelete="CASCADE"), nullable=False)
    film_genre_id = Column(String, ForeignKey("genres.id", ondelete="CASCADE"), nullable=False)

    films = relationship("Film")
    genres = relationship("Genre")