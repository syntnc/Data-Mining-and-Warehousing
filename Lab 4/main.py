import sys

import numpy as np
import pandas as pd

from naive_bayes import NaiveBayes


def import_data(filename):
    '''IMPORTS DATA FROM csv FILE'''
    dataset = pd.read_csv('data/' + filename, sep=',')
    headers = dataset.columns
    print('DATASET LENGTH\t:\t', len(dataset))
    print('DATASET SHAPE\t:\t', dataset.shape)
    return headers, dataset

def main():
    '''MAIN METHOD'''
    headers, dataset = import_data(sys.argv[1])
    print('\n{}'.format(dataset))
    dataset = dataset.as_matrix()
    X_train, y_train = np.array(dataset[:-1, :-1]), np.array(dataset[:-1, -1])
    test_data = np.array(dataset[-1, :-1])
    print('\n{}\t:\t{}'.format(headers[-1], NaiveBayes(X_train, y_train).classify(test_data)))

if __name__ == '__main__':
    main()
