from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, Item

#DB setup
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Test api endpoint
@app.route('/api/catagories/<int:catagory_id>/items/json')
def catagoryItemsJSON(catagory_id):
    catagory = session.query(Catagory).filter_by(id=catagory_id).one()
    items = session.query(Item).filter_by(catagory_id=catagory.id)
    return jsonify(Items=[i.serialize for i in items])

if __name__ == '__main__':
    app.secret_key = 'Puppies_puppies_puppies'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)