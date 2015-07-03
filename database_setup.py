from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#represents class as ORM class and helps to create database from schema
Base=declarative_base()

class Restaurant(Base):
	__tablename__='restaurant'
	id=Column(Integer,primary_key=True)
	name=Column(String(300),nullable=False)
	location=Column(String(300))
	contact=Column(Integer)
	
class MenuItem(Base):
	__tablename__='menu_item'
	id=Column(Integer,primary_key=True)
	name=Column(String(200))
	price=Column(String(8))
	restaurant_id=Column(Integer,ForeignKey('restaurant.id'))
	restaurant=relationship(Restaurant)
	

engine=create_engine('mysql+mysqlconnector://root:@localhost/mini_zomato')
Base.metadata.create_all(engine)
