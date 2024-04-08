questions = {
    0:{
        "question" : "DO YOU WANT TO KNOW BEST STATISTICAL TEST FOR YOUR DATA!! TELL US ABOUT YOUR DATA AND WE WILL HELP YOU OUT 😊",
        "options" : ["Start"],
        "next" : [1],
    },
    1: { # start
        "question": "IS THERE ONLY ONE VARIABLE OF INTEREST?🤔",
        "options": ["Yes", "No"],
        "next": [2, 7],
    },
    2: {
        "question": "WHAT ARE THE TOTAL NUMBER OF SAMPLES🤔",
        "options": ["1", "2" , "More than 2"],
        "next": [3 , 22 , 32],
    },
    3: {
        "question": "TYPE OF DISTRIBUTION🤔",
        "options": ["Normal", "Binomial", "Poisson", "Other"],
        "next": [4, 6, "ONE SAMPLE POISSON TEST", "USE ANOTHER UNDERLYING DISTRIBUTION OR USE NON-PARAMETRIC METHODS"],
    },
    4: {
        "question": "INFERENCE CONCERNING and KNOWNs?🤔",
        "options": ["Yes", "no" , "inference Concerning but not known"],
        "next": ["ONE SAMPLE Z TEST", "ONE SAMPLE CHI SQUARE TEST FOR VARIANCES(Caution: this test is very sensitive to normality)" , "ONE SAMPLE T TEST"],
    },
    5: { # not used 
        "question": "KNOWNS?🤔",
        "options": ["Yes", "No"],
        "next": ["ONE SAMPLE Z TEST", "ONE SAMPLE T TEST"],
    },
    6: {
        "question": "NORMAL APPROXIMATION VALID ??🤔",
        "options": ["Yes", "No"],
        "next": ["NORMAL THEORY METHODS", "EXACT METHODS"],
    },
    7: { # function 4
        "question": "INTERESTED IN RELATIONSHIP B.W 2 VARIABLES ??🤔",
        "options": ["Yes", "More Than 2 variables"],
        "next": [10, 8],
    },
    8: {
        "question": "OUTCOME VARIABLE CONTINOUS OR BINARY ??🤔",
        "options": ["Continous", "Binary"],
        "next": ["MULTIPLE REGRESSION METHODS", 9],
    },
    9: {
        "question": "TIME OF EVENTS IMPORTANT ??🤔",
        "options": ["Yes", "No"],
        "next": [27 , "MULTIPLE LOGISTIC REGRESSION METHODS"],
    },
    10: {
        "question": "What is the type of both variables ??🤔",
        "options": ["Continous", "1 continous and 1 categorical" , "both Ordinal" , "Both Categorical"],
        "next": [19 , 14 , "RANK COORELATION METHODS" , 13],
    },
    11: { #not used
        "question": "ONE VARIABLE CONTINOUS AND ONE CATEGORICAL ??🤔",
        "options": ["Yes", "No"],
        "next": [ 14, 12],
    },
    12: { #not used
        "question": "ORDINAL DATA ??🤔",
        "options": ["Yes", "No"],
        "next": ["RANK COORELATION METHODS" , 13],
    },

    13: {
        "question": "INTERESTED IN ASSOCIATION OR REPRODUCIBILITY ??🤔",
        "options": ["association", "reproducibility"],
        "next": ["USE CONTINGENCY TABLE METHODS", "USE KASPA STATISTIC"],
    },
    14: {
        "question": "NO. OF WAYS OF CLASSIFIFCATION OF THE CATEGORICAL VARIABLES??🤔",
        "options": ["1", "2" , "more than 2"],
        "next": [18, 16, 17],
    },
    15: {
        "question": "OTHER COVARIATES TO BE CONTROLLED FOR  ??🤔",
        "options": ["Yes", "No"],
        "next": ["1 WAY ANCOVA", "1 WAY ANOVA"],
    },
    16: {
        "question": "OTHER COVARIATES TO BE CONTROLLED FOR  ??🤔",
        "options": ["Yes", "No"],
        "next": ["2 WAY ANCOVA", "2 WAY ANOVA"],
    },
    17: {
        "question": "OTHER COVARIATES TO BE CONTROLLED FOR ??🤔",
        "options": ["Yes", "No"],
        "next": ["HIGHER WAY ANCOVA", "HIGHER WAY ANOVA"],
    },
    18: {
        "question": "NORMAL DISTRIBUTION  ??🤔",
        "options": ["Yes", "No"],
        "next": [15, "NON PARAMETRIC TEST , KRUSKAL WALLIS TEST"],
    },
    19: {
        "question": "INTERESTED IN PREDICTING ONE VARABLE FROM OTHER   ??🤔",
        "options": ["Yes", "No"],
        "next": ["SIMPLE LINEAR REGRESSION", 20],
    },
    20: {
        "question": "BOTH VARIABLES NORMAL  ??🤔",
        "options": ["Yes", "No"],
        "next": ["PEARSON CORRELATION METHODS", "RANK CORRELATION METHODS"],
    },
    21: { #function 1
        "question": "2 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": [22, 32],
    },
    22: {
        "question": "TYPE OF DISTRIBUTION  ??🤔",
        "options": ["normal", "Binomial" , "other"],
        "next": [26 , 24 , 23],
    },
    23: {
        "question": "PERSONS-TIME DATA ??🤔",
        "options": ["Yes", "No"],
        "next": [27  , "USE ANOTHER UNDERLYING DISTRIBUTION OR USE NON PARAMETRIC TEST"],
    },
    24: {
        "question": "SAMPLES INDEPENDENT ??🤔",
        "options": ["Yes", "No"],
        "next": [25 , "USE MC NEMARS TEST"],
    },
    25: {
        "question": "ALL EXPECTED VALUES >=5  ??🤔",
        "options": ["Yes", "No"],
        "next": [34 , "USE FISCHERS TEST"],
    },
    26: {
        "question": "INFERENCES CONCERNING MEANS  ??🤔",
        "options": ["Yes", "No"],
        "next": [36 , "2 SAMPLE F TEST TO COMPARE VARIANCES"],
    },
    27: {  # function 5 
        "question": " 1 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": ["1 SAMPLE TEST FOR INCIDENCE RATES", 28],
    },
    28: {
        "question": "INCIDENCE RATES CONSTANT OVER TIME ??🤔",
        "options": ["Yes", "No"],
        "next": [29, 30],
    },

    29: {
        "question": "A  2 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE 2 SAMPLE TEST FOR COMPARISION OF INCIDENCE RATES , IF NO CONFOUNDING IS PRESENT OR METHODS FOR STRATIFIED PERSON TIME DATA OF CONFOUNDING IS PRESENT", "USE OF TREND OF INCIDENCE RATE"],
    },
    30: {
        "question": "INTERESTED IN COMPARISION OF SURVIVAL CURVES OF 2 GRPS WITH LIMITED CONTROL OF VARIANCES  ??🤔",
        "options": ["Yes", "No"],
        "next": ["LOG RANK TEST", 31],
    },
    31: {
        "question": "WILLING TO ASSUME SEVERAL CURVE COMES FROM A WEIBULL DISTRIBUTIONS ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE PARAMETER SURVIVAL METHODS BASED ON WEIBULL DISTRIBUTION", "USE COX PROPORTIONAL HAZARDS MODEL"],
    },
    32: {  #function 2
        "question": "NORMAL DISTRBUTION  ??🤔",
        "options": ["Yes", "No"],
        "next": ["ONE WAY ANNOVA", 33],
    },
    33: {
        "question": "CATEGORICAL DATA  ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE R X C CONTINGENCY TABLE METHODS", "USE NON PARAMETRIC TEST LIKE KRUSKALL WALLIS OR OTHER DISTRIBUTION"],
    },
    34: { # function 6 
        "question": "TYPE OF CONTIGENCY TABLE ??🤔",
        "options": ["a 2 X 2 contingency table", "2 X k contingency table" , "R X C contingency table"],
        "next": ["USE 2 SAMPLE T TEST FOR BINOMIAL PROPORTIONS OR 2 X 2 CONTINGENCY TABLE METHODS OF NO COFOUNDING IS PRESENT OR MANTEL HAENSZEL TEST IF COFOUNDING IS PRESENT", 35 , "CHI SQUARE TEST FOR R X C TABLES"],
    },
    35: { #function B
        "question": "INTERESTED IN TREND OVER K BINOMIAL PROPORTIONS  ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE CHI SQUARE TEST FOR HETEROGENEITY FOR 2 X K TABLES", "USE CHI SQUARE TEST FOR TREND , IF NO CONFOUNDING IS PRESENT , OR MANTEL EXTENSION TEST IF CONFOUNDING IS PRESENT"],
    },
    36: {  #function 3
        "question": " SAMPLES INDEPENDENT ??🤔",
        "options": ["Yes", "No"],
        "next": [37, "USE PAIRED T TEST"],
    },
    37: {
        "question": "VARIANCE OF 2 SAMPLES SIGNIFICANTLY DIFFERENT(USING F TEST) ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE 2 SAMPLE T TEST WITH UNEQUAL VARIANCES", "USE 2 SAMPLED T TEST WTH EQUAL VARIANCES"],
    },
}