# Lab Assignment 4<!-- omit in toc -->
## Bayesian Classifier: Naive Bayes<!-- omit in toc -->
![Language](https://img.shields.io/badge/language-Python3-brightgreen.svg) ![Editor](https://img.shields.io/badge/VS%20Code-1.10.2-blue.svg) ![Institute](https://img.shields.io/badge/Institute-IIITA-yellow.svg) ![Course Code](https://img.shields.io/badge/Course%20Code-IDMW632C-red.svg) 

### Contents

- [Background](#background)
- [Assignments](#assignments)
  - [Programming Assignment](#programming-assignment)
  - [Theory Assignment](#theory-assignment)
___
## Background

The purpose of this assignment is to implement the technique of predicting results of unknown data using the *Naive Bayes* classification algorithm *without the usage of external libraries with pre-implemented algorithms*.

## Assignments

### Programming Assignment

Given the **Table A**, predict a class label buys_computer using naïve Bayesian classification for the tuple:

```
X = {  
        age = “<= 30”, 
        income = “medium”,
        student = “yes”, 
        credit_rating = “fair”
    }`
```

**Table A:**

Age | Income | Student | Credit_rating | Buys_computer
-|-|-|-|-
<=30 | High | No | Fair | No
<=30 | High | No | Excellent | No
31...40 | High | No | Fair | Yes
&gt;40 | Medium | No | Fair | Yes
&gt;40 | Low | Yes | Fair | Yes
&gt;40 | Low | Yes | Excellent | No
31...40 | Low | Yes | Excellent | Yes
<=30 | Medium | No | Fair | No
<=30 | Low | Yes | Fair | Yes
&gt;40 | Medium | Yes | Fair | Yes
<=30 | Medium | Yes | Excellent | Yes
31...40 | Medium | No | Excellent | Yes
31...40 | High | Yes | Excellent | Yes
&gt;40 | Medium | No | Excellent | No

**Solution**

```
python main.py table_a.csv
```

**Note**: Keep all csv files to test the algorithm on inside the `data` directory.

### Theory Assignment

A theme park hired you after graduation. Assume that you want to predict when the theme park receives lots of visitors. You gathered the following data:

||Feature 1<br>Sunny| Feature 2<br>High Temperature| Feature 3<br>Weekend| Feature 4<br>Lots of Visitors|
|-------|-----|-----|-----|-----|
| Day 1 | yes | yes | yes | yes |
| Day 2 | yes | no  | yes | yes |
| Day 3 | no  | yes | no  | yes |
| Day 4 | yes | yes | no  | yes |
| Day 5 | yes | yes | no  | yes |
| Day 6 | yes | no  | no  | no  |
| Day 7 | no  | no  | yes | no  |

What's the probability that the learned Bayesian network will predict that the theme park receives lots of visitors on a cloudy and hot weekend day?