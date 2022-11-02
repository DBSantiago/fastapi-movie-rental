from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class GenderModel(Base):
    """Cast gender database representation."""
    __tablename__ = "cast_genders"

    id = Column(Integer, primary_key=True)
    gender = Column(String(60), nullable=False, unique=True)
    members = relationship("MemberModel", back_populates="gender", lazy=True)
