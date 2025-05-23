from flask import Flask
from app.extensions import db
from datetime import datetime


class Students():
    __tableName__ = "Students"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime,  default = datetime.utcnow)
    updated_at = db.Column(db.DateTime,  onupdate = datetime.utcnow())

    #foregn_keys
    program_id= db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)

    # Relationship to student
    books = db.relationship('student', back_populates='program')

    def __init__(self, id, first_name, last_name, email, password, created_at, updated_at):
       self.id = id
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.password = password
       self.created_at = created_at
       self.updated_at = updated_at

        









