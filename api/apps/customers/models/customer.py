from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class CustomerModel(Base):
    """Customer database representation."""
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    orders = relationship("OrderModel", back_populates="customer", lazy=True)
