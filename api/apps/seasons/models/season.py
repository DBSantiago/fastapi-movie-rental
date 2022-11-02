from sqlalchemy import (
    Column, Integer, ForeignKey, UniqueConstraint,
)
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class SeasonModel(Base):
    """Season object database representation."""
    __tablename__ = "seasons"
    __table_args__ = (
        UniqueConstraint('series_id', 'number',
                         name='unique_season_number'),
    )

    id = Column(Integer, primary_key=True)
    series_id = Column(Integer, ForeignKey('films.id'),
                       nullable=False, )
    number = Column(Integer, nullable=False, )

    series = relationship("FilmModel", back_populates="seasons", lazy=True)
    episodes = relationship('EpisodeModel', back_populates='season', lazy=True)
