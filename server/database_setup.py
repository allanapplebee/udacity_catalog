import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#define classes for Catagory and Item
class Catagory(Base):
    __tablename__ = 'catagory'
    name = Column(
        String(50),
        nullable = False
    )
    id = Column(
        Integer,
        primary_key = True
    )

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class Item(Base):
    __tablename__ = 'item'
    
    cat_id = Column(
        Integer,
        ForeignKey('catagory.id')
    )
    description = Column(
        String(500),
        nullable = False
    )
    id = Column(
        Integer,
        primary_key = True
    )
    title = Column(
        String(50),
        nullable = False
    )
    catagory = relationship(Catagory)

    @property
    def serialize(self):
        return {
            'description': self.description,
            'id': self.id,
            'title': self.title
        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)