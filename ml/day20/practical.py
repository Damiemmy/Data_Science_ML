import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


model=LinearRegression()

data = {
    "study_hours": [2, 3, 5, 7, 8],
    "attendance": [65, 70, 90, 95, 98],
    "score": [55, 70, 75, 82, 91]
}

df=pd.DataFrame(data)

print(df)

X=df[["study_hours","attendance"]]
y=df["score"]

print(X)
print(y)

# model.fit(X,y)
'''
coefficient=model.coef_
interception=model.intercept_

print(coefficient)
print(interception)
'''

# prediction=model.predict(X)
# print(prediction)

'''
residuals= y-prediction
print("RESIDUALS: ",residuals)
'''

X_train,X_test,Y_train,Y_test=train_test_split(
  X,
  y,
  test_size=0.2,
  random_state=42
)

model.fit(X_train,Y_train)
prediction=model.predict(X_test)
print(prediction)

mae=mean_absolute_error(Y_test,prediction)
rmse=np.sqrt(mean_absolute_error(Y_test,prediction))

print("MAE: ",mae)
print("RMSE: ",rmse)
