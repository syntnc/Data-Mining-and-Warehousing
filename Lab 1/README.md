# Lab Assignment 1<!-- omit in toc -->
## Apriori Algorithm<!-- omit in toc -->
![Language](https://img.shields.io/badge/language-Python3-brightgreen.svg) ![Editor](https://img.shields.io/badge/VS%20Code-1.10.2-blue.svg) ![Institute](https://img.shields.io/badge/Institute-IIITA-yellow.svg) ![Course Code](https://img.shields.io/badge/Course%20Code-IDMW632C-red.svg) 

### Contents

- [Background](#background)
- [Assignments](#assignments)
    - [Basic Assignment](#basic-assignment)
    - [Additional Assignment](#additional-assignment)
___
## Background

The purpose of this assignment is to implement the technique of finding frequent itemsets using the *Apriori* algorithm and, using this information, generate the association rules which have support and confidence above certain minimum thresholds.

## Assignments

### Basic Assignment

Assume that an input file named **`transactions.txt`** consists of text that looks as follows:

```
1 3 4
1 2 3 5
2 3 5
2 5
1 2 3 6
```

In the file, blanks separate items (identified by integers) and new lines separate transactions. For example, the above file contains information about a total of 5 transactions and its second transaction consists of 4 items.

Your task is to write a program, in your favourite programming language, that takes as parameters the minimum support, minimum confidence (given as floating point numbers in the range `[0, 1]`), and the name of the file of transactions (whose format is as that of the **`transactions.txt`** above) and produces *all* association rules which can be mined from the transactions file which satisfy the minimum support and confidence requirements.

The rules should be output sorted first by the number of items that they contain (in decreasing order), then by confidence, and finally by their support (in decreasing order).
An example of a possible session using your program on the data of file **`transactions.txt`** is given below:

```
> myApriori -s 0.25 -c 0.58 transactions.txt

Mined transactions.txt
and found a total of 16 association rules:
========================================
    Rule        Confidence      Support
========================================
1 2 ==> 3       1                0.4
3 5 ==> 2       1                0.4
1 ==> 2 3       0.666            0.4
1 3 ==> 2       0.666            0.4
2 3 ==> 1       0.666            0.4
5 ==> 2 3       0.666            0.4
2 3 ==> 5       0.666            0.4
2 5 ==> 3       0.666            0.4
1 ==> 3         1                0.6
5 ==> 2         1                0.6
3 ==> 1         0.75             0.6
2 ==> 3         0.75             0.6
3 ==> 2         0.75             0.6
2 ==> 5         0.75             0.6
5 ==> 3         0.666            0.4
1 ==> 2         0.666            0.4
```

**Note**: If it makes your life any easier, you can assume that item numbers will be integers in the range `[0, 2^16 - 1]` and items appear once per transaction and sorted (as above). However, you cannot make any assumptions about the number of transactions that the file may contain.

**Solution**
```
python apriori.py -s <minimum support> [-c] <minimum confidence> <file name>
```

**Options:**
- **`-s --min_support`**: Minimum support threshold for association rules [default: `0.25`]
- **`-c --min_confidence`**: Minimum confidence threshold for association rules [default: `0.5`]
- File name of transactions to mine [default: `transactions.txt`]

### Additional Assignment

A database has five transactions. Let minimum support = 60% and minimum confidence = 80%.<br>
Find all frequent itemsets using *Apriori*.

|  TID  |    Items Bought    |
| ----  | ------------------ |
| T100  | {M, O, N, K, E, Y} |
| T200  | {D, O, N, K, E, Y} |
| T300  | {M, A, K, E}       |
| T400  | {M, U, C, K, Y}    |
| T500  | {C, O, O, K, I, E} |

**Solution**
```
python apriori.py -s <minimum support> [-c] <minimum confidence> <file name>
```

**Options:**
- **`-s --min_support`**: Minimum support threshold for association rules [default: `0.6`]
- **`-c --min_confidence`**: Minimum confidence threshold for association rules [default: `0.8`]
- File name of transactions to mine [default: `transactions.txt`]