import pandas as pd
import csv
import numpy as np

#reading the same csv file using pandas
df=pd.read_csv("students_dirty.csv")
print(df)
#🔎 DAY 7 — CHALLENGE 1: INSPECT THE DATA
print(df.info())
#🔎 CHALLENGE 2 — QUICK STATISTICS
print(df.describe())
#🔎 CHALLENGE 3 — FIND MISSING VALUES
print(df.isnull())
#🔥 CHALLENGE 4 — COUNT THE MISSING VALUES
print(df.isnull().sum())
#🧠 CHALLENGE 5 — WHICH ROWS HAVE MISSING DATA?
#I tried axis=0 and axis=1 and here is my finding i get to understand axis=0 is same thing as having no axis at all e.g df.isnull().any()) is same thing as print(df.isnull().any(axis=0))  both does the same thing by confirming if there's null value in table headers e.g name=True/False, age=True/False, and score=True/False. but using axis=1 returns the records each row that has a False value be it name,age or score.
'''
print(df.isnull().any(axis=0)) 
print(df.isnull().any()) 
'''
print(df.isnull().any(axis=1)) 
print(df[df.isnull().any(axis=1)]) 

#⚔️ CHALLENGE 6 — WHICH ROWS ARE COMPLETE?

print(df[df.notnull().all(axis=1)]) #return all values that are not Null
