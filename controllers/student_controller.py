from flask import Flask, Blueprint

#Creating the students blueprint
student_bp=Blueprint('students', 'student_bp', url_prefix='/students/')

#Defining the routes under the students blueprint
@student_bp.route('/student', methods=['POST'])
def add_student():
   #Empty list to store the new student
   students=()
   pass

#Fetching all students
@student_bp.route('/all_students', methods=['GET'])
def get_all_students():
   pass

#Deleting a student using its id
@student_bp.route('/<int:student.id', methods=['DELETE'])
def delete_program(id):
   pass
