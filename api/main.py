# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask , render_template , redirect , jsonify , request , session
from flask_cors import CORS
import pandas as pd

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)	

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/' , methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():  
	data = {"message": "STATSII"}
	return jsonify(data)

@app.route('/' , methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def hello_world2():  
	data = {"message": "DEVELOPER: TANISHQ TIWARI"}
	return jsonify(data)

from questions import questions
from filequestions import file_questions



@app.route('/question/<int:id>', methods=['GET'])
def get_question(id):
    # print(id)
    if id not in questions:
        return jsonify({'error': 'Invalid question ID'})
    current_question = questions[id]
    # print(current_question)
    return jsonify(current_question)


@app.route('/filequestion/<int:id>', methods=['GET'])
def get_filequestion(id):
    print(file_questions)
    # print(id)
    if id not in file_questions:
        return jsonify({'error': 'Invalid question ID'})
    current_question = file_questions[id]
    # print(current_question)
    return jsonify(current_question)



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    print(file)

    df = pd.read_csv(file)

    # Extract column names
    column_names = df.columns.tolist()

    # Print column names
    print(column_names)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Here you can process the uploaded file as per your requirements
    # For example, save it to a specific location, perform analysis, etc.

    return jsonify({'message': 'File uploaded successfully'})