'''DECISION TREE'''

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

def import_data():
    '''IMPORTS DATASET FROM csv FILE'''
    dataset = pd.read_csv('dataset.csv', sep=',')
    print('\nDATASET LENGTH\t:\t', len(dataset))
    print('DATASET SHAPE\t:\t', dataset.shape)
    return dataset

def split_dataset(dataset):
    '''SPLITS THE DATASET INTO TRAINING AND TESTING SETS'''
    X = dataset.values[:, 0:4]
    Y = dataset.values[:,4]
    X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.2, random_state = 100)
    return X, Y, X_train, X_test, y_train, y_test

def train_model(X_train, X_test, y_train, criterion):
    '''TRAINS DECISION TREE MODEL USING SPECIFIED CRITERION'''
    clf = DecisionTreeClassifier(criterion=criterion, random_state=100)
    clf.fit(X_train, y_train)
    return clf

def prediction(X_test, clf_object):
    '''PREDICTS RESULTS ON TESTING SET BASED ON CLASSIFICATIONS'''
    y_pred = clf_object.predict(X_test)
    print('PREDICTED VALUES:', y_pred, sep='\n')
    return y_pred

def main():
    '''MAIN METHOD'''
    dataset = import_data()
    X, Y, X_train, X_test, y_train, y_test = split_dataset(dataset)
    clf_gini = train_model(X_train, X_test, y_train, criterion="gini")
    clf_entropy = train_model(X_train, X_test, y_train, criterion="entropy")

    print('\n\nRESULTS:')

    print('\nGINI INDEX :')
    y_pred_gini = prediction(X_test, clf_gini)
    print('ACCCURACY =', accuracy_score(y_test, y_pred_gini))
    
    print('\nENTROPY:')
    y_pred_entropy = prediction(X_test, clf_entropy)
    print('ACCCURACY =', accuracy_score(y_test, y_pred_entropy))

if __name__ == '__main__':
    main()
