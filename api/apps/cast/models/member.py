from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class MemberModel(Base):
    """Cast member database representation."""
    __tablename__ = "cast_members"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    gender_id = Column(Integer, ForeignKey('cast_genders.id'),
                       nullable=False)
    role_id = Column(Integer, ForeignKey('cast_roles.id'),
                     nullable=False)

    gender = relationship("GenderModel", back_populates="members")
    role = relationship("RoleModel", back_populates="members")
