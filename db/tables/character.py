from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    comment = Column(String)
    name = Column(String, nullable=False)
    film_id = Column(Integer, ForeignKey("films.id", ondelete="CASCADE"), nullable=False)

    films = relationship("Film")
