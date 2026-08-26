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

