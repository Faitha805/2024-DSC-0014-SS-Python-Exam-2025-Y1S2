from flask import Flask, Blueprint

#Creating the programs blueprint
program_bp=Blueprint('programs', 'program_bp', url_prefix='/programs/')

#Defining the routes under the program blueprint
@program_bp.route('/', methods=['POST'])
def new_program():
   pass

#Updating a program using its id
@program_bp.route('/<int:program.id', methods=['PUT'])
def update_programn(id):
   pass