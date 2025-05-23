from flask import Flask
from app.extensions import db
from datetime import datetime


class Course():
    __tablename__ = "Course"
    id = db.Column(db.Integer,primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime,  default = datetime.utcnow)
    updated_at = db.Column(db.DateTime,  onupdate = datetime.utcnow())

    #foregn_keys
    student_id= db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=True)

    # Relationship to course
    books = db.relationship('course', back_populates='program')

    def __init__(self, id, name, email,created_at, updated_at):
       self.id = id
       self.name = name
       self.email = email
       self.created_at = created_at
       self.updated_at = updated_at

        









