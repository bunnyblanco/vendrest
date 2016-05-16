from sqlalchemy import (
        Column,
        Boolean,
        Integer,
        String,
        Text,
        Float,
        DateTime,
        ForeignKey,
        )
from vendcli.models.meta import Base

class Invoice(Base):
    __tablename__='tbl_receipt'
    id = Column(Integer, primary_key=True)
    supply_id = Column(Integer, ForeignKey('tbl_receipt.id'))
    name = Column(String(20), nullable=False) #The name/number
    amount = Column(Float, default=0.00)
    have = Column(Boolean)

class Expense(Base)
    __tablename__ = 'tbl_expense'
    id = Column(Integer, primary_key=True)
    trans_id = Column(Integer, ForeignKey('tbl_transaction.id'))
    ref_id = Column(Integer, ForeignKey(''tbl_receipt.id'))
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    merchandise = Column(Float, default=0.00)
    newspaper = Column(Float, default=0.00)
    supply = Column(Float, default=0.00)
    other = Column(Float, default=0.00)

