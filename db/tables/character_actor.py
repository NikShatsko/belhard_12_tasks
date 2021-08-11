from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class CharacterActor(Base):
    __tablename__ = "characters_actor"

    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)

    characters = relationship("Character")
    persons = relationship("Person")