from sqlalchemy import (
        Column,
        Float,
        Integer,
        String,
        Text,
        DateTime,
        ForeignKey,
        )
from vendcli.models.meta import Base

class Resource(Base):
    __tablename__='tbl_resource'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    type = Column(String(5), nullable=False) #REG, VEND, SAFE, BANK, CARD
    description = Column(Text)
    capital = Column(Float, default=0.00)

class Transaction(Base):
    __tablename__='tbl_transact'
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('tbl_resource.id'))
    name = Column(String(20), nullable=False) #CASH, EFT, check no.
    type = Column(String(5), nullable=False) #CREDIT, DEBIT, DEPOSIT, PULL, FCO
    timestamp = Column(DateTime, nullable=False)
    amount = Column(Float, default=0.00)
    description = Column(Text)

