questions = {
    0:{
        "question" : "DO YOU WANT TO KNOW BEST STATISTICAL TEST FOR YOU DATA!! TELL US ABOUT YOUR DATA AND WE WILL HELP YOU OUT 😊",
        "options" : ["START"],
        "next" : [1],
    },
    1: { # start
        "question": "IS THERE ONLY ONE VARIABLE OF INTEREST?🤔",
        "options": ["Yes", "No"],
        "next": [2, 7],
    },
    2: {
        "question": "IS THIS A ONE-SAMPLE PROBLEM?🤔",
        "options": ["Yes", "No"],
        "next": [3, 20],
    },
    3: {
        "question": "TYPE OF DISTRIBUTION🤔",
        "options": ["Normal", "Binomial", "Poisson", "Other"],
        "next": [4, 6, "ONE SAMPLE POISSON TEST", "USE ANOTHER UNDERLYING DISTRIBUTION OR USE NON-PARAMETRIC TEST"],
    },
    4: {
        "question": "INFERENCE CONCERNING?🤔",
        "options": ["Yes", "no"],
        "next": [5, "ONE SAMPLE CHI SQUARE TEST FOR VARIANCES"],
    },
    5: {
        "question": "KNOWNS?🤔",
        "options": ["Yes", "No"],
        "next": ["ONE SAMPLE Z TEST", "ONE SAMPLE T TEST"],
    },
    6: {
        "question": "NORMAL APPROXIMATION VALID ??🤔",
        "options": ["Yes", "No"],
        "next": ["NORMAL THEORY METHODS", "EXACT METHOD"],
    },
    7: { # function 4
        "question": "INTERESTED IN RELATIONSHIP B.W 2 VARIABLES ??🤔",
        "options": ["Yes", "No"],
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
        "next": [26 , "MULTIPLE LOGISTIC REGRESSIONS"],
    },
    10: {
        "question": "BOTH VARIABLE CONTINOUS ??🤔",
        "options": ["Yes", "No"],
        "next": [18 , 11],
    },
    11: {
        "question": "ONE CONTINOUS ANS ONE CATEGORICAL ??🤔",
        "options": ["Yes", "No"],
        "next": [ 14, 12],
    },
    12: {
        "question": "ORDINAL DATA ??🤔",
        "options": ["Yes", "No"],
        "next": ["RANK COORELATION METHODS" ,"13"],
    },

    13: {
        "question": "INTERESTED IN ASSOCIATION OR REPRODUCIBILITY ??🤔",
        "options": ["association", "reproducibility"],
        "next": ["CONTINGENCY TABLE METHODS", "KASPA STATISTIC"],
    },
    14: {
        "question": "NO. OF WAYS OF CLASSIFIFCATION OF THE CATEGORICAL VARIABLES??🤔",
        "options": ["1", "2" , "more than 2"],
        "next": [17, 15 , 16],
    },
    15: {
        "question": "OTHER COVARIATES TO BE CONTROLLED FOR  ??🤔",
        "options": ["Yes", "No"],
        "next": ["2 WAY ANCOVA", "2 WAY ANOVA"],
    },
    16: {
        "question": "OTHER COVARIATES TO BE CONTROLLED FOR ??🤔",
        "options": ["Yes", "No"],
        "next": ["HIGHER WAY ANCOVA", "HIGHER WAY ANOVA"],
    },
    17: {
        "question": "NORMAL DISTRIBUTION  ??🤔",
        "options": ["Yes", "No"],
        "next": [15, "NON PARAMETRIC TEST , KRUSKAL WALLIS TEST"],
    },
    18: {
        "question": "INTERESTED IN PREDICTING ONE VARABLE FROM OTHER   ??🤔",
        "options": ["Yes", "No"],
        "next": ["SIMPLE LINEAR REGRESSION", 19],
    },
    19: {
        "question": "BOTH VARIABLES NORMAL  ??🤔",
        "options": ["Yes", "No"],
        "next": ["PEARSON CORRELATION METHODS", "RANK CORRELATION METHODS"],
    },
    20: { #function 1
        "question": "2 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": [21, 32],
    },
    21: {
        "question": "DISTRIBUTION  ??🤔",
        "options": ["normal", "Binomial" , "other"],
        "next": [25 , 23 , 22],
    },
    22: {
        "question": "PERSONS-TIME DATA ??🤔",
        "options": ["Yes", "No"],
        "next": [26  , "USE ANOTHER UNDERLYING DISTRIBUTION OR USE NON PARAMETRIC TEST"],
    },
    23: {
        "question": "SAMPLES INDEPENDENT ??🤔",
        "options": ["Yes", "No"],
        "next": [24 , "USE MC NEMARS TEST"],
    },
    24: {
        "question": "ALL EXPECTED VALUES >=5  ??🤔",
        "options": ["Yes", "No"],
        "next": [33 , "USE FISCHERS TEST"],
    },
    25: {
        "question": "INFERENCES CONCERNING MEANS  ??🤔",
        "options": ["Yes", "No"],
        "next": [35 , "2 SAMPLE F TEST TO COMPARE VARIANCES"],
    },
    26: {  # function 5 
        "question": " 1 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": ["1 SAMPLE T TEST FOR INCIDENCE RATES", 27],
    },
    27: {
        "question": "INCIDENCE RATES CONSTANT OVER TIME ??🤔",
        "options": ["Yes", "No"],
        "next": [28, 29],
    },

    28: {
        "question": "A  2 SAMPLE PROBLEM ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE 2 SAMPLE TEST FOR COMPARISION OF INCIDENCE RATES , IF NO CONFOUNDING IS PRESENT OR METHODS FOR STRATIFIED PERSON TIME DATA OF CONFOUNDING IS PRESENT", "USE OF TREND OF INCIDENCE RATE"],
    },
    29: {
        "question": "INTERESTED IN COMPARISION OF SURVIVAL CURVES OF 2 GRPS WITH LIMITED CONTROL OF VARIANCES  ??🤔",
        "options": ["Yes", "No"],
        "next": ["LOG RANK TEST", 30],
    },
    30: {
        "question": "WILLING TO ASSUME SEVERAL CURVE COMES FROM A WEIIBULL DISTRIBUTIONS ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE PARAMETER SURVIVAL METHODS BASED IN WEIBULL DISTRIBUTION", "USE COX PROPORTIONAL HAZARDS MODEL"],
    },
    31: {  #function 2
        "question": "NORMAL DISTRBUTION  ??🤔",
        "options": ["Yes", "No"],
        "next": ["ONE WAY ANNOVA", 32],
    },
    32: {
        "question": "CATEGORICAL DATA  ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE R X C CONTINGENCY TABLE METHODS", "USE NON PARAMETRIC TEST LIKE KRUSKALL WALLIS OR OTHER DISTRIBUTION"],
    },
    33: { # function 6 
        "question": "TYPE OF CONTIGENCY TABLE ??🤔",
        "options": ["a 2 X 2 contingency table", "2 X k contingency table" , "R X C contingency table"],
        "next": ["USE 2 SAMPLE T TEST FOR BINOMIAL PROPORTIONS OR 2 X 2 CONTINGENCY TABLE METHODS OF NO COFOUNDING IS PRESENT OR MANTEL HAENSZEL TEST IF COFOUNDING IS PRESENT", 34 , "CHI SQUARE TEST FOR R X C TABLES"],
    },
    34: { #function B
        "question": "INTERESTED IN TREND OVER K BINOMIAL PROPORTIONS  ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE CHI SQUARE TEST FOR HETEROGENEITY FOR 2 X K TABLES", "USE CHI SQUARE TEST FOR TREND , IF NO CONFOUNDING IS PRESENT , OR MANTEL EXTENSION TEST IF CONFOUNDING IS PRESENT"],
    },
    35: {  #function 3
        "question": " SAMPLES INDEPENDENT ??🤔",
        "options": ["Yes", "No"],
        "next": [36, "USE PAIRED T TEST"],
    },
    36: {
        "question": "VARIANCE OF 2 SAMPLES SIGNIFICANTLY DIFFERENT(USING F TEST) ??🤔",
        "options": ["Yes", "No"],
        "next": ["USE 2 SAMPLE T TEST WITH UNEQUAL VARIANCES", "USE 2 SAMPLED T TEST WTH EQUAL VARIANCES"],
    },
}