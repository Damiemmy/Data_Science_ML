from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


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
model.fit(X,y)
prediction=model.predict(X)
print(f"features are {X}\n and predictions are {y}")
print("prediction= \n",prediction)

residuals=y-prediction
absolute_error=abs(y-prediction)
print("Residuals:\n",residuals)
print("Absolute_Errors:\n",absolute_error)

MAE= mean_absolute_error(y,prediction)
print("MAE:\n",MAE)

MSE= mean_squared_error(y,prediction)
print("MSE:\n",MSE)

RMSE=np.sqrt(mean_squared_error(y,prediction))
print("RMSE:\n",RMSE)

#VALIDATION SET
'''
1. Validation Set

A single train/test split has a weakness.

Suppose we do:

80% TRAIN
20% TEST

What if we got an unusually easy or unusually difficult test set?

Our measurement could be unstable.

So we can introduce a third partition:

                 DATA
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     TRAIN       VALIDATION   TEST
       70%          15%        15%
        │            │           │
        ↓            ↓           ↓
      Learn       Tune/choose   Final
                  model          evaluation
Training set

Used to learn parameters.

Validation set

Used to make development decisions.

For example:

Should I use Linear Regression or another model?

Should I change a hyperparameter?

Which feature configuration should I use?

Test set

Used for the final unbiased-ish evaluation after you've finished making model decisions.

'''