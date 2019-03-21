from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catagory, Base, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#add dummy data
catagory1 = Catagory(name="Skiing")
session.add(catagory1)
session.commit()

item1 = Item(description="Nice skis", title="Skis", catagory=catagory1)
session.add(item1)
session.commit()

item2 = Item(description="Nice gloves", title="Gloves", catagory=catagory1)
session.add(item2)
session.commit()

catagory2 = Catagory(name="Football")
session.add(catagory2)
session.commit()

item3 = Item(description="Nice balls", title="Balls", catagory=catagory2)
session.add(item3)
session.commit()

item4 = Item(description="Nice gloves", title="Glovess", catagory=catagory2)
session.add(item4)
session.commit()

print("Added cats and items")

