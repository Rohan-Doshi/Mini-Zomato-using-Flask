from flask import Flask,render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database_setup import Restaurant,MenuItem

Base=declarative_base()

engine=create_engine('mysql+mysqlconnector://root:@localhost/mini_zomato')
Base.metadata.bind = engine

DBsession=sessionmaker(bind=engine)
session=DBsession()

#create instance of flask app
app=Flask(__name__)

@app.route('/')
def home():
	list=session.query(Restaurant).all()
	return render_template('index.html',restra_list=list)

@app.route('/<int:restra_id>/')
def show_items(restra_id):
	restra_info=session.query(Restaurant).filter_by(id=restra_id).one()
	item_list=session.query(MenuItem).filter_by(restaurant_id=restra_id)
	return render_template('details.html',item_list=item_list,restra_info=restra_info)


#check if progg is ran by the python interpretor only
if __name__=="__main__":
	app.debug=True
	app.run('0.0.0.0',8000) #application will run on all public ip of system 


