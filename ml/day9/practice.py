import pandas as pd

data = {
    "name": ["John", "Mary", "David", "Sarah", "Peter"],
    "age": ["20", "19", "twenty", "20", "22"],
    "score": ["75", "82", "90", "ninety", "55"]
}
# Challenge 1 — Identify the Problem
df=pd.DataFrame(data)
print(df)
print(df.dtypes)

age=pd.to_numeric(df["score"],errors="coerce")

print(df.notnull().all())