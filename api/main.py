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
		return function4()
	
	ans = 1 ## one sample prroblem
	if(ans == 0):
		return function1()
	

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
	elif(ans == 4):
		print("use another underlying distribution or use non parameteric test")
		return
		

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
	ans = 1 # 2 sample problem
	if(ans == 0):
		return function2()
	

	ans = 1 # normal distribution
	if(ans == 2): 
		ans = 1 # samples independent
		if(ans == 0 ):
			print("Use McNemars test")
			return
		ans = 1 # all expected values >=5
		if(ans == 0):
			print("Use Fischers test")
		return function6()
	elif(ans == 3):
		ans = 1 # person-time data
		if(ans == 0):
			print("use another underlying distribution or use non parameteric test")
		return function5()
			

	ans = 1 #inferences concerning means
	if(ans == 0):
		print("2 sample F test to compare variances")
		return
	return function3()


def function2():
	ans = 0 # not normal distribution
	if(ans == 1):
		print("one way Annova")
		return
	ans = 0 # not categorical data
	if(ans == 1):
		print("Use R X C contingency table methods")
	print("use non parametric test like Kruskall Wallis or other distribution")
	return



def function3():
	ans = 1 # samples independent
	if(ans == 0 ):
		print("Use Paired T test")
		return
	ans = 1 # variance of 2 samples significantly different(USing F test)
	if(ans == 0):
		print("Use 2 samped T test wth equal variances")
	print("use 2 sample t test with unequal variances")
	return


def function4():
	ans = 1 # interested in realtionship b.w 2 variables
	if(ans == 0):
		ans = 1 #outcome variable continous
		if(ans == 0): # binary
			ans = 1 #time of events important
			if(ans == 0):
				print("Multiple Logistic regression")
				return 
			print("Survival Analysis methods")
			return function5()
		
	ans = 1 #both variable continous
	if(ans == 0): 
		ans = 1 #one continous ans one categorical
		if(ans == 0):
			ans = 1 #ordinal data
			if(ans == 0): # categorical
				ans = 1 #interested in association
				if(ans == 0): #interested in reproducibility
					print("Kaspa statistic")
					return
				print("Contingency table methods")
				return
			print("Rank coorelation methods")
			return
		print("Analysis of ANNOVA")
		ans = 1 # no. of ways of classififcation of the data
		if(ans == 2):
			ans = 1 # other variates to be controlled for
			if(ans == 0):
				print("2 way ANOVA")
				return
			print("2 way ANCOVA")
			return
		elif(ans > 2):
			ans = 1 # other variates to be controlled for
			if(ans == 0):
				print("Higher way ANOVA")
				return
			print("hfgher way ANCOVA")
			return
		ans = 1 # normal distribution
		if(ans == 0):
			print("NON parametric test , Kruskal Wallis Test")
			return 
		ans = 1 # other variates to be controlled for
		if(ans == 0):
			print("2 way ANOVA")
			return
		print("2 way ANCOVA")
		return
	
	ans = 0 #interested in predicting one varable from other 
	if(ans == 1):
		print("SIMPLE linear regression")
		return
	print("interested in studying the coorelation b/w 2 variables")
	ans = 1 # both variiables normal
	if(ans == 0):
		print("rank correlation methods")
		return
	print("pearson Correlation Methods")
	return
	



def function5():
	ans = 0 # not one sample problem 
	if(ans == 1):
		print("1 sample t test for incidence rates")
		return 
	ans = 1 # incidence rates constant over time
	if(ans == 0):
		print("Use Survival instincts methods")
		ans = 0 # not interested in comparision of survival curves of 2 grps with limited control of variances
		if(ans == 1):
			print("log rank Test")
		print("interested in effects of several risk factors on survival")
		ans = 1 # willing to assume several curve comes from a weiibull distributions
		if(ans == 0):
			print("Use Cox proportional hazards model")
			return
		print("use parameter survival methods based in weibull distribution")
		return
	ans = 0 # not a  2 sample problem
	if(ans == 1):
		print("use 2 sample test for comparision of incidence rates , if no confounding is present or methods for stratified person time data of confounding is present")
		return
	print("interested in test of trend over more than 2 exposure grps")
	print("use of trend of incidence rate")
	return



def function6():
	ans = 1 # a 2 X 2 contingency table
	if(ans == 1):
		return functionA()
	if(ans == 2): # 2 X k contingency table
		return functionB()
	else: # R X C contingency table
		print("chi square test for R X C tables")
		return

		
def functionA():
	print("use 2 sample t test for binomial proportions or 2 X 2 contingency table methods of no cofounding is present or Mantel Haenszel test if cofounding is present")
	return 


def functionB():
	ans = 1 # interested in trend over k binomial proportions
	if(ans == 0):
		print("use Chi sware test for trend , if no confounding is present , or Mantel Extension Test if confounding is present")
		return 
	print("use chi square test for heterogeneity for 2 X k tables")
	return


# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
