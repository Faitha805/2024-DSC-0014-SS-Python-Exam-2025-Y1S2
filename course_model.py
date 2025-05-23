from flask import Flask
from app.extensions import db
from datetime import datetime

#Creating the course model
class Course(db.Model):
    __tablename__='courses'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False, unique=True)
    lecturer=db.Column(db.String(100), nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)
    program_id=db.Column(db.Integer, ForeignKey='Program.id')
    #program=relationship('Program', backref='program') # creating a backref relationship

def __init__(self, name, lecturer):
    self.name=name
    self.lecturer=lecturer