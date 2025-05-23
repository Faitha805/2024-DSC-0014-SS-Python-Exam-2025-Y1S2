from flask import Flask, Blueprint

#Creating the programs blueprint
course_bp=Blueprint('courses', 'course_bp', url_prefix='/courses/')

#Defining the routes under the course blueprint
@course_bp.route('/course', methods=['POST']) #POST method used to create a new program
def add_course():
   course=() #Empty list to store the new program
   pass
