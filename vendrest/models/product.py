from sqlalchemy import (
        Column,
        Integer,
        String,
        Float,
        Text,
        DateTime,
        ForeignKey,
        )
from vendrest.models.meta import Base

class Product(Base):
    __tablename__='tbl_product'
    id = Column(Integer, primary_key=True)
    name = Column(String(12), nullable=False)
    size = Column(String(8))
    pack_count = Column(Integer, default=0)

class ProductCost(Base):
    __tablename__='tbl_cost'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('tbl_product.id'))
    pack_cost=Column(Float, default=0.00)
    unit_cost = Column(Float, default=0.00)

class Purveyor(Base):
    __tablename__ = 'tbl_supply'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    account = Column(String(20), nullable=False)
    pnum = Column(String(10), unique=True, nullable=False)
    email = Column(Text)
    saddress = Column(Text)
    saddress2 = Column(Text)
    city = Column(String(20))
    state = Column(String(2))
    postal = Column(String(9))

class Catalog(Base):
    __tablename__='tbl_catalog'
    id = Column(Integer, primary_key=True)
    supply_id = Column(Integer, ForeignKey('tbl_supply.id'))
    ITEM_num = Column(String(20))
    product_id = Column(Integer, ForeignKey('tbl_product.id'))

