from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class RoleModel(Base):
    """Cast role database representation."""
    __tablename__ = "cast_roles"

    id = Column(Integer, primary_key=True)
    role = Column(String(120), nullable=False, unique=True)
    members = relationship("MemberModel", back_populates="role", lazy=True)
