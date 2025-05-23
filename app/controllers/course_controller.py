from flask import Flask, Blueprint, request, jsonify
from app.models.course_model import Course
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_403_FORBIDDEN,HTTP_404_NOT_FOUND,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR
import validators

#Registering blueprints
course = Blueprint('course', __name__, url_prefix='/api/v1/auth')

# 1. student Registration
app = Flask(__name__)

course = []

# Creating a new student (POST)

@course.route('/register', methods=['POST'])
def register_course():
    data = request.json
    id = data.get('id')
    name = data.get('first_name')
    email = data.get('email')
 
   
# Validations
    if not id or not name or not email:
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST

    if len(id) < 8:
        return jsonify({"error": "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({"error": "Email is not valid"}), HTTP_400_BAD_REQUEST

    if Course.query.filter_by(email=email).first():
        return jsonify({"error": "Email address already in use"}), HTTP_409_CONFLICT


    course.append(course)
    return jsonify(course), HTTP_201_CREATED

if __name__ == '__main__':
    app.run(debug=True)