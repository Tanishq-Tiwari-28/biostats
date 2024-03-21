# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask , render_template , redirect , jsonify
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
	data = {"message": "Hello from Flask!"}
	return jsonify(data)

def start():
	ans = 1 # only 1 variable of interest
	if(ans == 0):
		function4()
		return 
	ans = 1 ## one sample prroblem
	if(ans == 0):
		function1()
		return 
	ans = 1 ## normal distribution
	if(ans == 2): #binomial
		ans = 1 # normal approximation valid
		if(ans == 0):
			print("exact method page 253")
			return
		print("Normal Theory methods pages 250=251")
		return
	elif(ans == 3): #poission
		print("one sample poission test")
		return
	else:
		print("use another underlying distribution or use non parameteric test")
		
	ans = 1 # inference conerning
	if(ans == 0):
		print("one sample chi square test")
		return
	ans = 1 # known
	if(ans == 0 ):
		print("one sample t test")
		return
	print("one sample Z test")
	return 
	
	




def function1():
	return
def function2():
	return
def function3():
	return
def function4():
	return
def function5():
	return
def function6():
	return
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
