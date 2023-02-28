from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import socket
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
# create the extension
# db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
engine = create_engine("mysql://ipc:ipcadmin@localhost:3306/instance_1")
Base = declarative_base()
class User(Base):
    __tablename__ = "ipc_users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
Session = sessionmaker(bind=engine)
session = Session()
# Function to fetch hostname and ip 
def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def hello_world():
    #Base.metadata.create_all(engine)
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    # Add a record
    session.add(User(username="John Doe3",password="John Doe3"))
    session.commit()

# Query records
    user = session.query(User).get(1)
    return jsonify(
        name=user.username,
        id=user.password
    )
@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)


@app.route("/authenticate")
def authenticate():
    users = {}
    i=0
    for instance in session.query(User):
        users[i] = {
                    'username':instance.username,
                    'password':instance.password
                    }
        i=i+1

    
    return users


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String)