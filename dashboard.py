import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# Modeling Packages
import sklearn
from sklearn.model_selection import train_test_split   # For Data Partitioning
from sklearn.linear_model import LinearRegression      # To implement Linear Regression
from sklearn.feature_selection import RFE              # To implement RFE
from sklearn.model_selection import StratifiedKFold, KFold              # For creating folds
from sklearn.model_selection import cross_val_score    # For implementing Cross Validation experiments
from sklearn.model_selection import GridSearchCV       # To implement GridSearch CV
from sklearn.model_selection import RandomizedSearchCV # To implement Randomized Search CV
from sklearn.linear_model import Lasso, Ridge          # To implement Lasso and Ridge Regression
from sklearn.metrics import classification_report
#from sklearn.metrics import plot_confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings('ignore')

def getAge():
    options = ['18-20', '21-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65 up']
    selected_option = st.radio("Select Age Range:", options)
    st.write(f"You selected: {selected_option}")

def getEduc():
    options = ['9 to 11', '12 or GED', '0 to 8', '12+ ', 'Special Ed']
    selected_option = st.radio("Select Education Level:", options)
    st.write(f"You selected: {selected_option}")

def getEthnic():
    options = ['Not of Hispanic or Latino origin', 'Other Hispanic or Latino origin', 'Mexican', 'Puerto Rican']
    selected_option = st.radio("Select Ethnicity:", options)
    st.write(f"You selected: {selected_option}")

def getRace():
    options = ['White', 'Other/Mutliple', 'Black or African American', 'Native', 'Asian','Pacific Islander']
    selected_option = st.radio("Select Race:", options)
    st.write(f"You selected: {selected_option}")

def getGender():
    options = ['Male', 'Female']
    selected_option = st.radio("Select Gender:", options)
    st.write(f"You selected: {selected_option}")

def getMarital():
    options = ['Never married', 'Now married', 'Divorced, widowed', 'Seperated']
    selected_option = st.radio("Select Marital Status:", options)
    st.write(f"You selected: {selected_option}")

def main():
    fileName = "data.csv"
    df = pd.read_csv(fileName).dropna()
    st.title("Predicting Mental Health Disorder from Demographic Information")
    userInput =  ['AGE', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
    answers = []
    def ask(header, options):
        selected_option = st.radio("Select" + header + " :", options)
        #st.write(f"You selected: {selected_option}")
        answers.append(selected_option)

    for i in range(len(userInput)):
        header = userInput[i]
        options = df[header].unique()
        ask(header, options)


    answers.insert(0, "1207979")
    answers.insert(2, "Trauma-related")
    st.write(answers)

def backend():
    fileName = "data.csv"
    df = pd.read_csv(fileName).dropna()
    df_copy = df.copy()
    #model = " "
    model = getModel(df)
    input = ['1207979', "60-64", "Trauma-related" , "12+", "Not of Hispanic or Latino origin", "White","Male", "Now married", "No", "Unemployed", "Private residence", "1", "CD"]
    prediction = getPrediction(df_copy, model, input)
    return prediction

if __name__ == '__main__':
    main()

"""

#clean input to a row
#feed row and get prediction
#streamlit input
#output: score, prediction
#how each input demographic is in comparison to the rest of the datasets for the Prediction
 """

def getPrediction(df, model, input):
    cols =  ["Unnamed: 0", 'AGE', 'MH1', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
    df.iloc[0] = input
    df_dummies = pd.get_dummies(df.drop(columns = ['MH1', 'Unnamed: 0']), drop_first = True)
    queryRow = np.array(df_dummies.iloc[0]).reshape(1, -1)
    prediction = model.predict(queryRow)
    #print('Score: ', model.best_score_)
    #print('Parameters: ', model.best_params_)
    return prediction

def getModel(df):
    input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
    df.iloc[0] = input
    x = pd.get_dummies(df.drop(columns = ['MH1', 'Unnamed: 0']), drop_first = True)
    y = df['MH1']
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.4, random_state = 1)
    folds = KFold(n_splits = 5, shuffle = True, random_state = 1)
    clf = DecisionTreeClassifier(random_state = 42)

    hyper_params_new = {
        'max_depth': list(range(50, 55)),
        'min_samples_split': list(range(1, 7)),
        'min_samples_leaf': list(range(42, 47))
    }

    # Call GridSearchCV()
    model_clf = GridSearchCV(estimator = clf,
                            param_grid = hyper_params_new,
                            scoring = 'f1_weighted', # Use a suitable regression metric
                            cv = folds,
                            verbose = 1,
                            n_jobs = -1) # Will utilize all available CPUs

    model_clf.fit(train_x, train_y)
    input = np.array(test_x.iloc[10]).reshape(1, -1)

    return model_clf
    #print('Improved score: ', model_clf.best_score_)
    #print('Improved parameters: ', model_clf.best_params_)



