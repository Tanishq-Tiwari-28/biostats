# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask , render_template , redirect , jsonify , request , session
from flask_cors import CORS

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



@app.route('/question/<int:id>', methods=['GET'])
def get_question(id):
    # print(id)
    if id not in questions:
        return jsonify({'error': 'Invalid question ID'})
    current_question = questions[id]
    # print(current_question)
    return jsonify(current_question)


@app.route('/answer', methods=['POST'])
def handle_answer():
    data = request.json
    question_id = int(data.get('question_id'))  # Convert to integer
    selected_option = int(data.get('selected_option'))  # Convert to integer
    print(question_id, selected_option)

    if question_id not in questions:
        return jsonify({'error': 'Invalid question ID'})

    next_question_or_result = questions[question_id]['next'][selected_option]

    # Check if the next is a string representing the final result
    if isinstance(next_question_or_result, str):
        return jsonify({'result': next_question_or_result})
    else:
        return jsonify({'next_question': next_question_or_result})


