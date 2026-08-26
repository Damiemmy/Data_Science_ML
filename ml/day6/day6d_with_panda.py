import pandas as pd
import csv
import numpy as np

#purpose of this code is to read a csv file and print the data in it using pandas and csv module
with open("students_dirty.csv","r") as file:
    reader=csv.DictReader(file) #dictionary reader
    '''
    reader=csv.reader(file) #list reader
    next(reader)  #used when "csv.reader" is used,it function is To Skip header which is the first line e.g name,age,score buts using csv.DictReader does this automatically for us
    '''
    for reader in reader:
        name=reader["name"]
        age=reader["age"]
        score=int(reader["score"])
        print(name,age,score)

#reading the same csv file using pandas
reader=pd.read_csv("students_dirty.csv")
print(reader)
