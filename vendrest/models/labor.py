from sqlalchemy import (
        Column,
        Integer,
        Float,
        String,
        Text,
        DateTime,
        ForeignKey,
        )
from vendrest import Base

class Schedule(Base):
    __tablename__='tbl_sched'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False) #day of the week or month or year
    time_in = Column(DateTime, nullable=False)
    time_out = Column(DateTime, nullable=False)
    hours = Column(Float, nullable=False)

class Employee(Base):
    __tablename__='tbl_employ'
    id = Column(Integer, primary_key=True)
    fname = Column(String(20), nullable=False)
    lname = Column(String(20), nullable=False)
    mname = Column(String(20))
    title = Column(String(12), nullable=False)
    hired = Column(DateTime, nullable=False)
    pay = Column(Float, nullable=False) #per hour
    sched_id = Column(Integer, ForeignKey('tbl_sched.id')

class TimeSheet(Base):
    __tablename__='tbl_labor'
    id = Column(Integer, primary_key=True)
    employ_id = Column(Integer, ForeignKey('tbl_employ.id'))
    date = Column(DateTime, nullable=False)
    sched_id = Column(Integer, ForeignKey('tbl_sched.id'))
    hours = Column(Float, nullable=False)

