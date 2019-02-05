# Lab Assignment 2<!-- omit in toc -->
## FP Growth Algorithm<!-- omit in toc -->
![Language](https://img.shields.io/badge/language-Python3-brightgreen.svg) ![Editor](https://img.shields.io/badge/VS%20Code-1.10.2-blue.svg) ![Institute](https://img.shields.io/badge/Institute-IIITA-yellow.svg) ![Course Code](https://img.shields.io/badge/Course%20Code-IDMW632C-red.svg) 

### Contents

- [Background](#background)
- [Assignment](#assignment)
___
## Background

The purpose of this assignment is to implement the technique of finding frequent itemsets using the *FP Growth* algorithm and, using this information by generating an *FP-tree* to enumerate the frequent patterns.

## Assignment

Construct an **FP-tree** using appropriate data set (use the some support count threshold) for association rule mining. Explain all the steps of the tree construction and draw the resulting tree.

Based on this tree answer the questions:

- How many transactions does it contain?
- Simulate frequent pattern enumeration based on the **FP-tree** constructed.
- Give comparative analysis of this process with Apriori algorithm.


**Note**: Download the datasets from either of the following links: | [Link 1](https://wiki.csc.calpoly.edu/datasets/wiki/apriori) | [Link2](http://fimi.ua.ac.be/data/) |

**Solution**
```
python fp_growth.py <dataset path> -s <minimum support>
```

**Options:**
- File path of the dataset of transactions to mine.
- **`-s --minimum-support`**: Minimum support count threshold for association rules [default: `2`]
