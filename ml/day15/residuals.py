import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = {
    "study_hours": [2, 3, 5, 7, 8],
    "attendance": [65, 70, 90, 95, 98],
    "score": [55, 70, 75, 82, 91]
}
df=pd.DataFrame(data)

print(df)

X=df[["study_hours","attendance"]]

y=df["score"]


model=LinearRegression()

model.fit(X,y)

print(model.coef_)
print(model.intercept_)
prediction=model.predict(X)
print("Prediction",prediction)



# Residuals = y-prediction
#what is residuals= is the prediction-error obtain which could be behind reality or far from reality, it shows directions with negative minus sign(-) or (+)
residuals = y-prediction
print(residuals)

#Absolute_Errors:absolute error removes direction from residuals. e.g if a residuals have 5,-5 calculating the average with that residuals might give you a 0 but with absolute_errors it's transform the output to 5,5 and average becomes accurate.
absolute_errors= abs(y-prediction)
print(absolute_errors)
#NOTE:
    '''
     with Residuals and no absolute_error the model could incorrectly conclude:
    "The model made no error." 😂

    It clearly did.

    The positive and negative errors merely cancelled each other.
    This leads us naturally to our first serious evaluation metric.
    '''


#⚔️ CHALLENGE 9 — THINK BEFORE USING A METRIC
'''
    Suppose a model makes these errors:

    +10
    -10
    +5
    -5
    A.

    If we simply calculate:

    mean(error)

    what happens?

    B.

    Would that be a good representation of how much error the model actually made? Why?

    C.

    What mathematical operation could we perform on each error first so that:

    +10

    and:

    -10

    both contribute 10 rather than cancelling each other?

    Don't look it up.
'''
1. if we calculate the mean error we would get 0 with the model concluding there was no error which is not true

2. by using absolute error brings out a good presentation of how much error the model made. reason is because if we don't use absolute error it would result to zero with the model working on the assumption there was not error most especially in case where there are both negative and positive prediction error output

3. abs(y-prediction), here y is the actual score  while prediction is the models predicted score


#⚔️ CHALLENGE 10 — ENGINEER'S QUESTION
'''
    Suppose I have two regression models.

    Model A:
    Actual:    [100, 100, 100]
    Predicted: [101, 101, 101]

    and:

    Model B:
    Actual:    [100, 100, 100]
    Predicted: [90, 110, 100]

    Both models have an average signed error of:

    0

    Would you consider that enough information to conclude that their predictions are equally good?

    Explain why.

'''
i won't conclude that prediction are equally good reasons are because model B didn't use absolute_errors to remove directions before calculating the average and this leads to no errors, if it could have implemented it the average would move from 10 +(-10)+0/3 =0 to 10+10+0/3=6.67,
and it same thing applicable to model A from -1 + -1 + -1/3 = -1 to 1 + 1 + 1/3 = 1 . to my best of knowledge and all you have taught me, this is how i could answer the question without googling or looking up as you said. review my answer and let's move to the next with pace leaving no stone unturned