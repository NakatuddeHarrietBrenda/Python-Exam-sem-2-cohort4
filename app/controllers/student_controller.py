from flask import Flask, Blueprint, request, jsonify
from app.models.student_model import Students
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_403_FORBIDDEN,HTTP_404_NOT_FOUND,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR
import validators


#Registering blueprints
program = Blueprint('program', __name__, url_prefix='/api/v1/auth')


# 1. student Registration

app = Flask(__name__)

students = []

# Creating a new student (POST)

@students.route('/register', methods=['POST'])
def register_student():
    data = request.json
    id = data.get('id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('location')
   
# Validations
    if not id or not first_name or not last_name or not email:
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST

    if len(password) < 8:
        return jsonify({"error": "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({"error": "Email is not valid"}), HTTP_400_BAD_REQUEST

    if Students.query.filter_by(email=email).first():
        return jsonify({"error": "Email address already in use"}), HTTP_409_CONFLICT


    students.append(students)
    return jsonify(students), HTTP_201_CREATED



#Fetching a student
@students.route('/students', methods=['GET'])
def get_products():
    return jsonify(students)


#Deleting a student
@students.route('/students/<int:id>', methods=['DELETE'])
def delete_studentt(id):
    global students
    students = [p for p in students if p['id'] != id]
    return jsonify({"message": "student deleted"})

if __name__ == '__main__':
    app.run(debug=True)