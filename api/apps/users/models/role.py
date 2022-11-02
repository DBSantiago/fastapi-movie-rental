from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class UserRoleModel(Base):
    """User rol database representation."""
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    role = Column(String(60), nullable=False, unique=True)
    permission_level = Column(Integer, nullable=False)

    users = relationship("UserModel", back_populates="role", lazy=True)
