questions = {
    1: { # start
        "question": "Is there only one variable of interest?",
        "options": ["Yes", "No"],
        "next": [2, 7],
    },
    2: {
        "question": "Is this a one-sample problem?",
        "options": ["Yes", "No"],
        "next": [3, 20],
    },
    3: {
        "question": "Type of Distribution",
        "options": ["Normal", "Binomial", "Poisson", "Other"],
        "next": [4, 6, "one sample poisson test", "use another underlying distribution or use non-parametric test"],
    },
    4: {
        "question": "Inference Concerning?",
        "options": ["Yes", "no"],
        "next": [5, "one sample chi square test for variances"],
    },
    5: {
        "question": "KNOWNs?",
        "options": ["Yes", "No"],
        "next": ["one sample Z test", "one sample t test"],
    },
    6: {
        "question": "normal approximation valid ??",
        "options": ["Yes", "No"],
        "next": ["Normal Theory methods", "exact method"],
    },
    7: { # function 4
        "question": "interested in relationship b.w 2 variables ??",
        "options": ["Yes", "No"],
        "next": [10, 8],
    },
    8: {
        "question": "outcome variable continous or binary ??",
        "options": ["Continous", "Binary"],
        "next": ["multiple Regression methods", 9],
    },
    9: {
        "question": "time of events important ??",
        "options": ["Yes", "No"],
        "next": [26 , "Multiple Logistic regressions"],
    },
    10: {
        "question": "both variable continous ??",
        "options": ["Yes", "No"],
        "next": [18 , 11],
    },
    11: {
        "question": "one continous ans one categorical ??",
        "options": ["Yes", "No"],
        "next": [ 14, 12],
    },
    12: {
        "question": "ordinal data ??",
        "options": ["Yes", "No"],
        "next": ["Rank coorelation methods" ,13],
    },

    13: {
        "question": "interested in association or reproducibility ??",
        "options": ["association", "reproducibility"],
        "next": ["Contingency table methods", "Kaspa statistic"],
    },
    14: {
        "question": "no. of ways of classififcation of the categorical variables??",
        "options": ["1", "2" , "more than 2"],
        "next": [17, 15 , 16],
    },
    15: {
        "question": "other covariates to be controlled for  ??",
        "options": ["Yes", "No"],
        "next": ["2 way ANCOVA", "2 way ANOVA"],
    },
    16: {
        "question": "other covariates to be controlled for ??",
        "options": ["Yes", "No"],
        "next": ["higher way ANCOVA", "Higher way ANOVA"],
    },
    17: {
        "question": "normal distribution  ??",
        "options": ["Yes", "No"],
        "next": [15, "NON parametric test , Kruskal Wallis Test"],
    },
    18: {
        "question": "interested in predicting one varable from other   ??",
        "options": ["Yes", "No"],
        "next": ["SIMPLE linear regression", 19],
    },
    19: {
        "question": "both variables normal  ??",
        "options": ["Yes", "No"],
        "next": ["pearson Correlation Methods", "rank correlation methods"],
    },
    20: { #function 1
        "question": "2 sample problem ??",
        "options": ["Yes", "No"],
        "next": [21, 32],
    },
    21: {
        "question": "distribution  ??",
        "options": ["normal", "Binomial" , "other"],
        "next": [25 , 23 , 22],
    },
    22: {
        "question": "persons-time data ??",
        "options": ["Yes", "No"],
        "next": [26  , "use another underlying distribution or use non parameteric test"],
    },
    23: {
        "question": "samples independent ??",
        "options": ["Yes", "No"],
        "next": [24 , "Use Mc Nemars test"],
    },
    24: {
        "question": "all expected values >=5  ??",
        "options": ["Yes", "No"],
        "next": [33 , "Use Fischers test"],
    },
    25: {
        "question": "Inferences concerning means  ??",
        "options": ["Yes", "No"],
        "next": [35 , "2 sample F test to compare variances"],
    },
    26: {  # function 5 
        "question": " 1 sample problem ??",
        "options": ["Yes", "No"],
        "next": ["1 sample t test for incidence rates", 27],
    },
    27: {
        "question": "incidence rates constant over time ??",
        "options": ["Yes", "No"],
        "next": [28, 29],
    },

    28: {
        "question": "a  2 sample problem ??",
        "options": ["Yes", "No"],
        "next": ["use 2 sample test for comparision of incidence rates , if no confounding is present or methods for stratified person time data of confounding is present", "use of trend of incidence rate"],
    },
    29: {
        "question": "interested in comparision of survival curves of 2 grps with limited control of variances  ??",
        "options": ["Yes", "No"],
        "next": ["log rank Test", 30],
    },
    30: {
        "question": "willing to assume several curve comes from a weiibull distributions ??",
        "options": ["Yes", "No"],
        "next": ["use parameter survival methods based in weibull distribution", "Use Cox proportional hazards model"],
    },
    31: {  #function 2
        "question": "normal Distrbution  ??",
        "options": ["Yes", "No"],
        "next": ["one way Annova", 32],
    },
    32: {
        "question": "categorical data  ??",
        "options": ["Yes", "No"],
        "next": ["Use R X C contingency table methods", "use non parametric test like Kruskall Wallis or other distribution"],
    },
    33: { # function 6 
        "question": "Type of Contigency Table ??",
        "options": ["a 2 X 2 contingency table", "2 X k contingency table" , "R X C contingency table"],
        "next": ["use 2 sample t test for binomial proportions or 2 X 2 contingency table methods of no cofounding is present or Mantel Haenszel test if cofounding is present", 34 , "chi square test for R X C tables"],
    },
    34: { #function B
        "question": "interested in trend over k binomial proportions  ??",
        "options": ["Yes", "No"],
        "next": ["use chi square test for heterogeneity for 2 X k tables", "use Chi sware test for trend , if no confounding is present , or Mantel Extension Test if confounding is present"],
    },
    35: {  #function 3
        "question": " samples independent ??",
        "options": ["Yes", "No"],
        "next": [36, "Use Paired T test"],
    },
    36: {
        "question": "variance of 2 samples significantly different(USing F test) ??",
        "options": ["Yes", "No"],
        "next": ["use 2 sample t test with unequal variances", "Use 2 samped T test wth equal variances"],
    },
}