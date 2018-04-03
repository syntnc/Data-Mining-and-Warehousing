'''BAYESIAN CLASSIFICATION - NAIVE BAYES CLASSIFIER'''

from collections import Counter, defaultdict

import numpy as np


class NaiveBayes(object):
    '''NAIVE BAYES CLASSIFIER CLASS'''
    
    def __init__(self, X, Y):
        self.labels = np.unique(Y)
        self.features =X.shape[1]
        self.likelihoods = self.initialize_likelihoods()
        self.class_probabilities = self.get_probability(Y) # PRIOR PROBABILITIES
        self.train(X, Y)

    @staticmethod
    def get_probability(outcome):
        '''RETURNS A DICTIONARY WITH PROBABILITIES OF THE OCCURENCES'''
        no_of_samples = len(outcome)
        probability = dict(Counter(outcome))
        for key in probability.keys():
            probability[key] /= no_of_samples
        return probability

    @staticmethod
    def create_subset(X, Y, label):
        '''CREATES SUBSET OF X BELONGING TO A PARTICULAR CLASS'''
        row_indices = np.where(Y == label)[0]
        return X[row_indices, :]

    @staticmethod
    def get_max_value_key(dictionary):
        '''RETURNS DICTIONARY KEY THAT HAS THE MAXIMUM VALUE'''
        return max(dictionary, key=dictionary.get)

    def initialize_likelihoods(self):
        return dict((label, defaultdict(list)) for label in self.labels)
    
    def train(self, X, Y):
        '''TRAINS THE CLASSIFIER'''

        # COUNT THE OCCURRENCES OF THE FEATURES, CLASS-WISE
        for label in self.labels:
            subset_X = self.create_subset(X, Y, label=label)
            for feature in range(self.features):
                self.likelihoods[label][feature] += list(subset_X[:, feature])

        # TRANSFORM THE TABLE OF COUNTS INTO TABLE OF PROBABILITIES
        for label in self.labels:
            for feature in range(self.features):
                self.likelihoods[label][feature] = self.get_probability(self.likelihoods[label][feature])

    def classify(self, X_test):
        '''PREDICTS CLASS LABEL FOR TEST DATA'''
        prediction = {}

        # DETERMINE CLASS PROBABILITY FOR EACH CLASS
        for label in self.labels:
            class_probability = self.class_probabilities[label]
            for feature in range(self.features):
                relative_feature_values = self.likelihoods[label][feature]
                if X_test[feature] in relative_feature_values.keys():
                    class_probability *= relative_feature_values[X_test[feature]]
                else:
                    class_probability = 0
            prediction[label] = class_probability

        # RETURN CLASS WITH THE MAXIMUM PROBABILITY AS THE PREDICTION
        return self.get_max_value_key(prediction)
