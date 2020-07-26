# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:47:01 2019

"""
import xgboost
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model.logistic import LogisticRegression
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model.logistic import LogisticRegression
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score, confusion_matrix, roc_auc_score, \
    matthews_corrcoef, roc_curve
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from xgboost.sklearn import XGBClassifier

auc = []
metrics1 = []


def scores(y_test, y_pred, th=0.5):
    y_predlabel = [(0 if item < th else 1) for item in y_pred]
    tn, fp, fn, tp = confusion_matrix(testy, y_predlabel).flatten()
    SPE = tn * 1. / (tn + fp)
    MCC = matthews_corrcoef(testy, y_predlabel)
    Recall = recall_score(testy, y_predlabel)
    Precision = precision_score(testy, y_predlabel)
    F1 = f1_score(testy, y_predlabel)
    Acc = accuracy_score(testy, y_predlabel)
    AUC = roc_auc_score(testy, y_pred)
    return [Recall, SPE, Precision, F1, MCC, Acc, AUC, tp, fn, tn, fp]

'''
trainData,testData 都是CsvData类的实例化
'''
def my_xgboost(trainData,testData):
    trainX = trainData.x
    trainy = trainData.y
    global testX,testy
    testX = testData.x
    testy =testData.y
    parameter_space = {"n_estimators": [10], "learning_rate": [0.1, 0.01, 0.001], "max_depth": [3, 30, 300],
                   "sample": [0.5, 1], "min_child_weight": [0, 1, 3, 5, 10, 15], "gamma": [0, 0.1, 1, 10, 100]}

    clf = GridSearchCV(estimator=XGBClassifier(random_state=100),
                   param_grid=parameter_space, cv=StratifiedShuffleSplit(n_splits=10, test_size=0.2,
                                                                         random_state=42), n_jobs=8, scoring='roc_auc')

    clf = clf.fit(trainX, trainy)
    print (clf.best_params_)
    # print (clf.best_score_)
    y_pred = clf.predict_proba(testX)[:, 1]
    # print(y_pred)
    testAUC = roc_auc_score(testy, y_pred)
    auc.append(testAUC)
    score = scores(testy, y_pred)
    metrics1.append(score)
    print(score)
