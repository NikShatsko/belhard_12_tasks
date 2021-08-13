from sqlalchemy import Column, Integer, ForeignKey


from ..base import Base


class CharacterActor(Base):
    __tablename__ = "characters_actor"

    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False, primary_key=True)
