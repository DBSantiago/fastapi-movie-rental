from sqlalchemy import Column, Integer, String

from api.db.base_class import Base


class FilmCategoryModel(Base):
    """Film category database representation."""
    __tablename__ = "film_categories"

    id = Column(Integer, primary_key=True)
    category = Column(String(60), nullable=False, unique=True)
