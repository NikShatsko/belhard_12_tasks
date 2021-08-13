from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from ..base import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(DateTime, nullable=False)

    character_actor = relationship(
        "Character",
        secondary="characters_actor",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"Person name = {self.name} {self.surname}"
