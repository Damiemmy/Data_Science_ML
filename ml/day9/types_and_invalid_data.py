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

# Challenge 2 — What Is The Type?
print(df["age"].dtype)
print(df["score"].dtype)

# Challenge 3 — Try Converting
'''print(pd.to_numeric (df["age"]))'''

#Challenge 4 — Tell Pandas How To Handle Invalid Values
print(pd.to_numeric(df["age"], errors="coerce"))


clean_age = pd.to_numeric(df["age"],errors="coerce")
clean_score = pd.to_numeric(df["score"],errors="coerce")
print("CLEAN AGE",clean_age)
print("CLEAN SCORE",clean_score)

'''
Note: Don't overwrite the originals yet for challenge 5.

Why? Because preserving the original data is an excellent engineering habit.

You want to be able to compare:

raw data
     ↓
cleaned data

instead of destroying the evidence.

'''

# Challenge 6 — Inspect Again

print(df,clean_age,clean_score)
print(df.dtypes)


'''
DAY 9 — THE FOUR TYPES OF PROBLEMS

Start building this mental framework.

1. Missing
age = NaN

Information is absent.

2. Invalid
age = "twenty"

Information exists, but isn't valid for the intended representation.

3. Inconsistent
Nigeria
NIGERIA
nigeria

Potentially the same category represented differently.

4. Outlier
age = 250

The value may technically be numeric, but it may not make sense in the domain.

These are different problems.

Therefore: They shouldn't automatically receive the same cleaning strategy.
'''
