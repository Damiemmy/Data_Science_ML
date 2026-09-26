from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
#First: Baselines
'''
Before I explain it, I want to test your reasoning.

Suppose we have:

Actual test scores:
[60, 70, 80, 90, 100]

The training-set average score was:

80

Therefore the baseline predicts:

[80, 80, 80, 80, 80]

Challenge:

Calculate the five absolute errors.
Calculate the baseline MAE.
Explain why comparing our ML model against this baseline is more informative than simply saying “our model has MAE = 5.”

'''

# answers 1
data={
  "score": [60, 70, 80, 90, 100]
}
df=pd.DataFrame(data)
print(df)
b=[80, 80, 80, 80, 80]
actual_score=df["score"]
baseline_prediction=actual_score.mean()
print("BP: ",baseline_prediction)
y=df["score"] - b

print("Absolute Errors: ", y)



absolute_error= mean_absolute_error(actual_score,baseline_prediction)

print(absolute_error)

