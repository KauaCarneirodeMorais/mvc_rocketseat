from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.slqlite.settings.base import Base # base decorativa

class PetsTable(Base):
    __tablename__ = "people"

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self):
        return (
    f"People [name={self.name}, "
    f"last_name={self.last_name}, type={self.type}, "
    f"pet_id={self.pet_id}]"
)
