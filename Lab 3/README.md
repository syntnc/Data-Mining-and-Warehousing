# Lab Assignment 3<!-- omit in toc -->
## Decision Tree<!-- omit in toc -->
![Language](https://img.shields.io/badge/language-Python3-brightgreen.svg) ![Editor](https://img.shields.io/badge/VS%20Code-1.10.2-blue.svg) ![Institute](https://img.shields.io/badge/Institute-IIITA-yellow.svg) ![Course Code](https://img.shields.io/badge/Course%20Code-IDMW632C-red.svg) 

### Contents

- [Background](#background)
- [Assignments](#assignments)
  - [Programming Assignment](#programming-assignment)
  - [Theory Assignment](#theory-assignment)
___
## Background

The purpose of this assignment is to implement the technique of predicting results of unknown data using the *Decision Tree* algorithm.

## Assignments

### Programming Assignment

In electronic commerce applications we want to make predictions about what a user will do.

Consider the following made-up data used to predict whether someone will ask for more information (`more_info`) based on whether they accessed from an educational domain (`edu`), whether this is a first visit (`first`), whether they have bought goods from an affiliated company (`bought`), and whether they have visited a famous online information store (`visited`).

| bought |  edu  | first | visited | more_info |
|--------|-------|-------|---------|-----------|
| false  | true  | false |  false  |   true    |
| true   | false | true  |  false  |   false   |
| false  | false | true  |  true   |   true    |
| false  | false | true  |  false  |   false   |
| false  | false | false |  true   |   false   |
| true   | false | false |  true   |   true    |
| true   | false | false |  false  |   true    |
| false  | true  | true  |  true   |   false   |
| false  | true  | true  |  false  |   false   |
| true   | true  | true  |  false  |   true    |
| true   | true  | false |  true   |   true    |
| false  | false | false |  false  |   true    |

We want to use this data to learn the value of `more_info` as a function of the values of the other variables.

**Solution**

Dependencies:

- numpy
- pandas
- scikit-learn

The `csv_writer.py` helps to create a csv of the above table. Once the `dataset.csv` file is generated, run the decision tree as follows:

```
python decision_tree.py
```

**Note:** Use matplotlib to plot the decision tree model, if asked for.

### Theory Assignment

Suppose we measure the error of a decision tree as the number of misclassified examples. The optimal decision tree from a class of decision trees is an element of the class with minimal error.

- Give the optimal decision tree with only one node. What is the error of this tree?

- Give the optimal decision tree of depth 2 (i.e., the root node is the only node with children). For each node in the tree give the examples that are filtered to that node. What is the error of this tree?

- Give the decision tree that is produced by the top-down induction algorithm run to completion, where we split on the attribute that reduces the error the most. For each node in the tree, specify which examples are filtered to that node. As well as drawing the tree, give the tree in terms of `if(Att,Then,Else)`.

- Give two instances that don't appear in the examples above and show how they are classified. Use this to explain the bias inherent in the tree (How does the bias give you these particular predictions?).

- How can overfitting occur in the learned network? Explain in terms of this example.
 