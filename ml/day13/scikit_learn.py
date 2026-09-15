import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "study_hours": [2, 3, 5, 7, 8],
    "attendance": [65, 70, 90, 95, 98],
    "score": [55, 70, 75, 82, 91]
}


df=pd.DataFrame(data)

print(df)

X = df[["study_hours", "attendance"]]
y = df["score"]

model = LinearRegression()

model.fit(X, y)

print(model.coef_)
print(model.intercept_)