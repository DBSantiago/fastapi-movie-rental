from sqlalchemy import (
    Column, Integer, ForeignKey, UniqueConstraint, String,
)
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class EpisodeModel(Base):
    """Episode object database representation."""
    __tablename__ = "episodes"
    __table_args__ = (
        UniqueConstraint('season_id', 'number',
                         name='unique_episode_number'),
    )

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    season_id = Column(Integer, ForeignKey('seasons.id'),
                       nullable=False)
    number = Column(Integer, nullable=False)

    season = relationship("SeasonModel", back_populates="episodes")
