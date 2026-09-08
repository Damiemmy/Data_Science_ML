import pandas as pd
import numpy as np

data = {
    "age": [20, 19, 21, 20, 22],
    "study_hours": [5, 7, 3, 8, 2],
    "attendance": [90, 95, 70, 98, 65],
    "score": [75, 82, 70, 91, 55]
}

df = pd.DataFrame(data)

print(df)
x=df[["age","study_hours","attendance"]]
y=df["score"]

print(f"X={x} and Y={y}")

df["attendance_rate"]=df['attendance']/100

df["study_efficiency"]=df['attendance']/df['study_hours']


df["high_attendance"]=df["attendance"]>=90




df["performance"]=np.where(
    df["score"]>=70,
    "Excellent",
    "needs improvement"
)

#np.where(condition, value_if_true, value_if_false)
print(df)
