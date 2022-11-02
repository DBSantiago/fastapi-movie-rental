from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table, Numeric, Date,
)
from sqlalchemy.orm import relationship

from api.apps.seasons.models import SeasonModel # noqa
from api.db.base_class import Base

films_x_categories_table = Table(
    "films_x_categories",
    Base.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("category_id", ForeignKey("film_categories.id")),
)

films_x_cast_members_table = Table(
    "films_x_cast_members",
    Base.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("cast_member_id", ForeignKey("cast_members.id")),
)


class FilmModel(Base):
    """Film type database representation."""
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    film_type_id = Column(Integer, ForeignKey('film_types.id'),
                          nullable=False)
    categories = relationship("FilmCategoryModel",
                              secondary=films_x_categories_table)
    price = Column(Numeric(precision=6, scale=2), nullable=False)
    stock = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)
    cast = relationship("MemberModel",
                        secondary=films_x_cast_members_table)

    film_type = relationship("FilmTypeModel", back_populates="films")
    seasons = relationship("SeasonModel", back_populates="series", lazy=True)
