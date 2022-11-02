from datetime import date
from decimal import Decimal

from sqlalchemy import (
    Column, Integer, ForeignKey, Numeric, Date, Boolean, Table,
)
from sqlalchemy.orm import relationship

from api.db.base_class import Base

films_x_orders_table = Table(
    "films_x_orders",
    Base.metadata,
    Column("film_id", ForeignKey("films.id")),
    Column("order_id", ForeignKey("orders.id")),
)


class OrderModel(Base):
    """Order object database representation."""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'),
                         nullable=False, )
    films = relationship("FilmModel",
                         secondary=films_x_orders_table, )
    rent_date = Column(Date, nullable=False, default=date.today())
    return_date = Column(Date, nullable=False, )
    penalty = Column(Numeric(precision=6, scale=2),
                     default=Decimal("0.00"), )
    total = Column(Numeric(precision=6, scale=2),
                   default=Decimal("0.00"), )
    returned = Column(Boolean, default=False)

    customer = relationship("CustomerModel", back_populates="orders")
