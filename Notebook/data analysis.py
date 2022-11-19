#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:32:34 2022

@author: danidlsa-u
"""


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
import numpy as np

#a. Load the data.

url= "https://raw.githubusercontent.com/MargheritaPhilipp/comp4ds_hw5/mph-changes/sample_diabetes_mellitus_data.csv"

data = pd.read_csv(url)

data.info()

#b. Split the data between train and test. (you can use train_test_split from sklearn or any other
#way)

# Leaving a function to split train/test after doing transformations

X_train, X_test, y_train, y_test= train_test_split(X, y, random_state = seed, train_size = .80)

def training(X, y):
    seed=1
    X_train, X_test, y_train, y_test= train_test_split(X, y, random_state = seed, train_size = .80)
    return X_train, X_test, y_train, y_test


#c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity.

data.dropna(subset=['age','gender', 'ethnicity'], inplace=True)    

#d. Fill NaN with the mean value of the column in the columns: height, weight.

vars_to_replace=['height', 'weight']

for v in vars_to_replace:
    data[v]= np.where(pd.isna(data[v])==True, 
                                   data[v].mean(),
                                   data[v])


#e. Generate dummies for ethnicity column (One hot encoding).

ethnicity = pd.get_dummies(data['ethnicity'], drop_first = True) 
data = data.join(ethnicity)


#f. Create a binary variable for gender M/F.

data["gender_dummy_male"] = pd.get_dummies(data["gender"], drop_first=True)

#g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the
#train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
#‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the
#column: ‘diabetes_mellitus’

features = ['age','height','weight','aids','cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
X = data.loc[:, features]
y = data.loc[:, ['diabetes_mellitus']]

X_train, X_test, y_train, y_test = training(X, y)

#Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create regressor
clf = LogisticRegression(random_state=0).fit(X_train, np.array(y_train["diabetes_mellitus"]))



#h. Predict the targets for both the train and test sets and add the prediction as a new column (use
#predict_proba from the model to get the predicted probabilities) name the new column something like predictions.

predict_train = clf.predict_proba(X_train)
predict_test = clf.predict_proba(X_test)

## New column to which dataset??


#i. Compute the train and test roc_auc metric using roc_auc_score from sklearn..

roc_auc_score(y_train, clf.predict_proba(X_train)[:, 1])

roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1])

