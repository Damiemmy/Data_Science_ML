import pandas as pd
import numpy as np
'''
🧪 DAY 7 MINI INVESTIGATION

Create:

day7_data_inspection.py

Load:students_dirty.csv

Then produce:
Dataset overview:
    - Shape
    - Columns
    - Data types
    - Info
Statistical overview
    - describe()
Missing-data analysis
    - isnull()
    - isnull().sum()

Missing rows
Find:students with at least one missing value.

Complete rows
Find:students with no missing values.
'''
df=pd.read_csv("students_dirty.csv")
print(df)
print("Shape",df.shape)
print("Column",df.shape[1])
print("Information",df.info())
print("Data Types",df.dtypes)
print("Statistical Overview",df.describe())
print("Missing Data", df.isnull())
print("Number of Missing Data",df.isnull().sum())
print("Missing Rows",df[df.isnull().any(axis=1)])
print("complete Rows",df[df.notnull().all(axis=1)])
print("Is Null Boolean Masking", df.isnull().any())
print("Total Null Count:",df.isnull().sum())
#during Boolean masking axis must be specified with value=1 e.g (axis=1) to carry out operation on code without bugs or errors this returns the rows with data that matches the condition
'''
print("Missing Rows",df[df.isnull().any()])
print("complete Rows",df[df.notnull().all()])

'''

#questions and answers
'''
1.Why do you think Pandas represents the missing numeric values as NaN?

2.Why might age become float64 even though ages are normally integers?

3.What is the difference between:
df.isnull() and:df.isnull().sum()

4.Why shouldn't we immediately delete every row containing missing data?
These questions are more important than the syntax.
'''

#answers
'''
question 1.) Pandas represents the missing numeric Values as NaN because by default values are strings,  missing values are converted to Not a Number(NaN). 2.) i still wonder why the integer age become float but my assumptions are based on mathematical operation, perharps calcultation are to be run on age values float is the best option because it welcome decimal values for accuracy. 3.)df.isnull() returns a boolean mask True or False statement if a value is NaN or rather if they are missing values while df.isnull().sum() returns,records or take note of the number of missing values in each column.  4.) delete every row that contain a missing data is not advisable without understanding the data, why it is missing and other condition, that would be a bad data engineering 

'''
#ASSIGNMENT CORRECTION:

    #1.)
    '''
    1. Why does Pandas use NaN?

    You said:"by default values are strings"
    That's the part I want to correct.

    Pandas does not represent missing numeric values as NaN because values are strings.
    Rather, when Pandas reads your CSV, it infers the data type of each column.
    For example:

    age
    20
    19
    21
    20
    22
    missing
    21

    Pandas recognizes this as fundamentally numeric data, but there's a missing entry.
    Historically, NaN is a floating-point representation for "not a number," and Pandas/NumPy commonly use it to represent missing numeric values.

    So think:
    CSV
    ↓
    Pandas parses values
    ↓
    Pandas infers dtype
    ↓
    missing numeric value
    ↓
    NaN
    '''

    #2.)

    '''
    2. Why did age become float64?

    Your reasoning about decimal calculations is understandable, but that's not why it happened.

    Consider:

    20
    19
    21
    20
    22
    NaN
    21

    A traditional NumPy integer array cannot naturally contain NaN.

    So the column gets represented as a floating-point array:

    20.0
    19.0
    21.0
    20.0
    22.0
    NaN
    21.0

    Notice:

    20 → 20.0

    The numerical value hasn't changed.

    The representation/type changed so the missing value can coexist with the numeric values.

    That's an important distinction.

    '''
'''
🧠 And You Just Learned Another Engineering Principle

Don't confuse:

Data value

with:

Data representation

For example:

20
20.0

represent the same mathematical quantity.

But Python/NumPy/Pandas may store them differently.

This will become important when we eventually discuss:

    - dtype
    - memory
    - precision
    - overflow
    - performance
    - numerical stability
'''