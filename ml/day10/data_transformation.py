import pandas as pd

data = {
    "age": [20, 19, 21, 20, 22],
    "study_hours": [5, 7, 3, 8, 2],
    "attendance": [90, 95, 70, 98, 65],
    "score": [75, 82, 70, 91, 55]
}

df = pd.DataFrame(data)

print(df)

#Challenge 2
age=df["age"]
study_hours=df["study_hours"]
attendance=df["attendance"]
score=df["score"]
X=df[["age","study_hours","attendance"]]
print("X",X)
print("y",score)

#CHALLENGE 3 — CREATE A NEW FEATURE
'''
FEATURES                 TARGET

age ───────────────┐
study_hours ───────┼──→ ML MODEL ──→ predicted score
attendance ────────┘
'''

# CHALLENGE 2 — CREATE X AND y
'''

Conventionally in ML you'll frequently see:

X → input features
y → target

Your job:

X = ?
y = ?

Don't worry about actually training a model yet.

We're simply learning to structure the data.

You should be able to inspect:

print(X)
print(y)

and explain exactly what each represents.

'''