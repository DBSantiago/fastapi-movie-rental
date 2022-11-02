from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class UserModel(Base):
    """User database representation."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(60), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    role_id = Column(Integer, ForeignKey('user_roles.id'),
                     nullable=False)

    role = relationship("UserRoleModel", back_populates="users")
