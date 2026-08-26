import numpy as np
import pandas as pd

data_pandas = {
    "age": [20, 19, 21, 20, 22],
    "study_hours": [5, 7, 3, 8, 2],
    "attendance": [90, 95, 70, 98, 65]
}
data_numpy=np.array([
    [20, 19, 21, 20, 22],
    [5, 7, 3, 8, 2],
    [90, 95, 70, 98, 65]
])


df = pd.DataFrame(data_pandas)

print(df)
print(df.columns)
print(df.shape)
print(df.dtypes)
print(df.ndim)
print(df.index)

dataset={
    "title": [1,2,3,4,5],
    "subject":[5,4,3,2,1],
    "reg_no":[9,8,2,2,4]
}

student=pd.DataFrame(dataset)
student_numpy=np.array([
    [6,7,8,0,9],
    [11,12,13,14,15]])

print(student)
print(student.columns)
print(student_numpy)
print(student.ndim)
print(student_numpy.ndim)


import pandas as pd
import numpy as np

student_info={
    "nin":[0,7,0,4,3],
    "phone":[7,7,7,4,8],
    "reg":[0,8,1,0,5]
}

df=pd.DataFrame(student_info)

print(df)
print(df.dtypes)
print(df.shape)
print(df.columns)
print(df.index)
print(student_numpy.dtype)
print(df["nin"])
df[df["attendance"] >= 90]