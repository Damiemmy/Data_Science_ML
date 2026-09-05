import pandas as pd

data = {
    "age": [20, 19, 21, 20, 22],
    "study_hours": [5, 7, 3, 8, 2],
    "attendance": [90, 95, 70, 98, 65],
    "score": [75, 82, 70, 91, 55]
}

df=pd.DataFrame(data)

reader=pd.read_csv("students_dirty.csv")


print("DATA:",df)
print("AGE",df["age"])
print("CSV:nv",reader)

age=reader["age"]
score=reader["score"]
print(reader.isnull().sum())

print("READER",reader.info())


