from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class FilmTypeModel(Base):
    """Film type database representation."""
    __tablename__ = "film_types"

    id = Column(Integer, primary_key=True)
    film_type = Column(String(60), nullable=False, unique=True)
    films = relationship("FilmModel", back_populates="film_type", lazy=True)
