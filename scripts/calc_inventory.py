from vendcli.models import (
        Product, 
        ProductCost
        )
from vendcli.models.meta import (
        Base,
        engine,
        Session,
        )

Base.metadata.create_all(engine)
session = Session()

p = Product(name='Snickers',pack_count=24)
session.add(p)
session.flush()

pc = ProductCost(product_id=p.id, pack_cost=15.00,unit_cost=0.62)
session.add(pc)
session.commit()
session.close()
