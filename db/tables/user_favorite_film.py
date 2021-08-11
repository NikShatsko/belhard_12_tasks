from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class UserFavoriteFilm(Base):
    __tablename__ = "user_favorite_films"

    user_login = Column(String, ForeignKey("users.login", ondelete="CASCADE"), nullable=False)
    film_id = Column(Integer, ForeignKey("films.id", ondelete="Cascade"), nullable=False)

    users = relationship("User")
    films = relationship("Film")