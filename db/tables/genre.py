from sqlalchemy import Column, String

from ..base import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(String, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"Genre name = {self.name}"




