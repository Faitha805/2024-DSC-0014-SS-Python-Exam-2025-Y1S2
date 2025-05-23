from flask import Flask
from app.extensions import db
from datetime import datetime

#Creating the student model
class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(100), nullable=False, unique=True)
    contact=db.Column(db.String(100), nullable=False, unique=True)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)
    program_id=db.Column(db.Integer, ForeignKey='Program.id')
    course_id=db.Column(db.Integer, ForeignKey='Course.id')

def __init__(self, name, email, contact):
    self.name=name
    self.email=email
    self.contact=contact


