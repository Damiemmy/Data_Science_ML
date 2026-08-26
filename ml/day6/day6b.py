import pandas as pd
import numpy as np
data_pandas = {
    "age": [20, 19, 21, 20, 22],
    "study_hours": [5, 7, 3, 8, 2],
    "attendance": [90, 95, 70, 98, 65]
}

df=pd.DataFrame(data_pandas)

data_numpy=np.array([
    [20,5,90],
    [19,7,95],
    [21,3,70],
    [20,8,98],
    [22,2,65],
])
ar=data_numpy

df= pd.DataFrame(data_pandas)

print(df)
print(ar)
print(df.shape)
print(ar.shape)
print(df.ndim)
print(ar.ndim)
print(df.dtypes)
print(ar.dtype)
attendance=df["attendance"]
attendance_numpy=data_numpy[:,2]
attendance_90_above=attendance_numpy >= 90
print(attendance_numpy)
print(data_numpy[attendance_90_above])
print(attendance)

# print(df[attendance >= 90])
print("Pandas:",df[(df["attendance"] >= 90) & (df["study_hours"] >= 5)])
print("Numpy:", data_numpy[data_numpy[:,2] >=90])

'''
Now calculate:

average age
average study hours
average attendance
highest attendance
lowest attendance
'''
#for pandas
print(df["age"].mean())
print(df["study_hours"].mean())
print(df["attendance"].mean())
print(df["attendance"].max())
print(df["attendance"].min())

#for numpy

print(np.mean(data_numpy[:,0]))
print(np.mean(data_numpy[:,1]))
print(np.mean(data_numpy[:,2]))
print(np.max(data_numpy[:,2]))
print(np.min(data_numpy[:,2]))

'''
🚨 CHALLENGE 6 — Your First Real Data Loading
This is where Pandas starts becoming extremely useful.

Take your existing:students_dirty.csv
and load it directly.

Think about: pd.read_csv(...)

Then:print(df)

Compare this to all the code you previously wrote with:

csv.DictReader(...)

This is an important moment.

You're going to realize:"Oh... Pandas handles a lot of this for me."

But don't interpret that as: "I didn't need to learn CSV."

You needed to learn CSV first because now you understand what's happening underneath the abstraction.

That's exactly how we're going to approach every layer of AI.
'''
