from flask import Flask #Importing the Flask class from flask library.
from app.extensions import db 
from datetime import datetime

#Creating a program class with it's attributes
class Program(db.Model):
    __tablename__='programs'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    duration=db.Column(db.String(100), nullable=True)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)

def __innit__(self, name, duration):
    self.name=name
    self.duration=duration
