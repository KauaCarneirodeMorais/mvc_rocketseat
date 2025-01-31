from sqlalchemy import Column, String, BIGINT
from src.models.slqlite.settings.base import Base # base decorativa

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"Pets [name={self.name}, type{self.type}]"
