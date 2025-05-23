from flask import Flask,  Blueprint, request, jsonify
from app.models.program_model import Program
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_403_FORBIDDEN,HTTP_404_NOT_FOUND,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR
import validators

#Registering blueprints
program = Blueprint('program', __name__, url_prefix='/api/v1/auth')

# 1.Program Registration

app = Flask(__name__)

program = []

#  program creation
@program.route('/register', methods=['POST'])
def register_program():
    data = request.json
    id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
  
   
# Validations
    if not id or not name or not email:
        return jsonify({"error": "All fields are required"}), HTTP_400_BAD_REQUEST

    if len(password) < 8:
        return jsonify({"error": "Password is too short"}), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({"error": "Email is not valid"}), HTTP_400_BAD_REQUEST

    if program.query.filter_by(email=email).first():
        return jsonify({"error": "Email address already in use"}), HTTP_409_CONFLICT


    program.append(program)
    return jsonify(program), HTTP_201_CREATED

#Updating a program
@app.route('/program', methods=['PUT'])
def get_programs():
    return jsonify(program)

    
