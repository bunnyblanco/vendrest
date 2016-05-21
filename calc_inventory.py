from vendrest.models import (
        Product, 
        ProductCost
        )
from vendrest.models.meta import (
        Base,
        engine,
        Session,
        )

Base.metadata.create_all(engine)
session = Session()

p = Product(name='Snickers',pack_count=24)
session.add(p)
session.flush()

pc = ProductCost(product_id=p.id, pack_cost=15.00,unit_cost=15.00/p.pack_count)
session.add(pc)
session.commit()
session.close()
