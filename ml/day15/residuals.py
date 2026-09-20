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
mae = absolute_errors.mean()
print("MAE:", mae)
#NOTe:
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
'''
1. if we calculate the mean error we would get 0 with the model concluding there was no error which is not true

2. by using absolute error brings out a good presentation of how much error the model made. reason is because if we don't use absolute error it would result to zero with the model working on the assumption there was not error most especially in case where there are both negative and positive prediction error output

3. abs(y-prediction), here y is the actual score  while prediction is the models predicted score
'''


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

'''
i won't conclude that prediction are equally good reasons are because model B didn't use absolute_errors to remove directions before calculating the average and this leads to no errors, if it could have implemented it the average would move from 10 +(-10)+0/3 =0 to 10+10+0/3=6.67,
and it same thing applicable to model A from -1 + -1 + -1/3 = -1 to 1 + 1 + 1/3 = 1 . to my best of knowledge and all you have taught me, this is how i could answer the question without googling or looking up as you said. review my answer and let's move to the next with pace leaving no stone unturned
'''

#⚔️ CHALLENGE 11 — INTERPRET MAE

'''
Suppose we get:

MAE = 3.2
for our student-score model.

What does:

MAE = 3.2
mean in the context of student scores?

Be careful.

Don't say:
"The model is 96.8% accurate."
That's not what MAE means.
Explain it in plain engineering language.
'''
MAE is the average or mean of the prediction error or residual in better context that was that was transformed into an absolute error for the purpose of revealing magnitude :


#⚔️ CHALLENGE 12 — COMPARE TWO MODELS:

'''
⚔️ CHALLENGE 12 — COMPARE TWO MODELS

Suppose:

Model A:
MAE = 2.1

Model B:
MAE = 5.7

What does the difference tell us?

Then answer this:

Can we immediately deploy Model A in a real university system simply because its MAE is lower?

Why or why not?

I want you to think beyond the metric.

'''
the difference tells us that model A has absolute_error with an average of 2.1
while model B has Absolute Errors with an average of 5.7

Based on my understanding i would for say 5.7 has higher MAE compared to 2.1,which means they are much error gap(residual) involve in Model B = 5.7 compare to model A = 2.1, but still i would only agree to deploy 2.1  only after ensuring that the model learnt training Data well enough and generalized well with unseen data 

# ⚔️ CHALLENGE 13 — THE TRAP

'''
Consider these two models:

Model A
Errors:
1
1
1
1
1
Model B
Errors:
0
0
0
0
5

Both have:

MAE = 1

What does this tell you?

And here's the harder question:

Does equal MAE necessarily mean the models make the same kinds of mistakes?

Explain.
'''
This tell me that the model average are both one,lolz

from personal observation i wouldn't say they make same kind of mistake, model A has consitent errors which from my own assumption i would say the model has learn complex patterns well enough to give same error output lol,Model B has no error for the first four data, but the last had error so, they didn't make same kind of mistake


#Correction
#11
Better interpretation:

MAE = 3.2 means that, on average, the model's predictions are 3.2 score points away from the actual student scores.

For example:

Actual:     75
Predicted:  72
Error:       3

It means: Average prediction error ≈ 3.2 score points

#⚔️ Challenge 14 — Before I teach you MSE

Suppose we have two prediction errors:

Model A → error = 2
Model B → error = 10
What does MAE see for each error?
What happens if we square both errors?
Why might squaring errors be useful when evaluating a model?
What potential problem could squaring errors introduce?

Don't look it up.

I want your engineering intuition first.