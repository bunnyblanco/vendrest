from vendcli.models import Resource, Transaction
from vendcli.models.meta import (
        Base, 
        engine, 
        Session
        )
import datetime

Base.metadata.create_all(engine)
session = Session()

e9 = Resource(name='E9',type='VEND',description='Ohare Cafe E9',capital=54.00)
bank = Resource(name='Checking Account',type='BANK',description='Business Checking Account',capital=0.00)
session.add(e9)
session.add(bank)

session.flush()

session.add(Transaction(source_id=e9.id,ref_code='CASH',type='PULL',amount=400.00,timestamp=datetime.datetime.today(),description='Thursday Cash Pull'))
session.flush()

session.commit()
session.close()
