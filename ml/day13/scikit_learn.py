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

#continuation from day 12

#Challenge 4
'''
    If you see something like: [3.2, 0.4]

    what does the first number correspond to?
    What does the second number correspond to?
    And why do you know that?
'''
- the first number corresponds to coefficient of study_hours.
- the second number corresponds to the coefficient of attendance.
- why i know that is because give X = df[["study_hours", "attendance"]], study_hours comes before attendance and we used model.coef_ to find each coefficient per unit feature in which it contributes to prediction holding other features constant


#Challenge 5:

'''
    Suppose the model learned:

    study_hours coefficient = 3
    attendance coefficient = 0.5
    intercept = 10

    Predict the score for:

    study_hours = 4
    attendance = 80

    Do it manually.

    Then tell me:

    What happens to the prediction if study_hours increases from 4 → 5 while attendance stays at 80?

    Don't just calculate it.

    Explain what the coefficient tells you.
'''

3*4+0.5*80 + 10 = 62

if study_hours increase from 4 to 5 while attendance remains constants at 80, the prediction increase per unit the coefficient of study hours.now what is the coefficient of study hours
coefficient_study_hours=3
prediction = 62
increase=4-3= 1
therefore prediction= 62 + (3*1)
=65


#Challenge 6:

'''
    Challenge 6: Principal Engineer Question

    Imagine I give you this model:

    score = 3 × study_hours + 0.5 × attendance + 10

    and someone tells you:

    "The model is 100% accurate, therefore it's an excellent model."

    Would you accept that statement?

    Why or why not?

    Don't look it up.

    I want your engineering instinct.
'''
alright lol, lets taste my engineering instinct,
-first of i would run a quick check first to verify the available input variable checking it's coefficient and intercept if its accurate.
if it is accurate, i would give the person a handshake but drop a message for that person saying "i wouldn't say this model is excellent, but alway have it at the back of your mind that the accuracy of a model depends on how much quality and quantitative data you feed into it, the more the data, the more accurate the prediction



# Correction Challenge 6:
⚔️ CHALLENGE 6 — 6.5/10
"""
    Now we need to do some serious correction.

    Your instinct to not blindly accept "100% accurate" was good.

    But these two parts need work.

    ❌ First problem

    You said you'd:

    "verify the available input variable checking it's coefficient and intercept if its accurate."

    Coefficients and intercept don't tell you whether the model is accurate.

    They're simply the parameters of the fitted model.

    Imagine:

    coefficient = 3
    intercept = 10

    That doesn't tell you whether the model makes good predictions.

    To investigate performance, we need to compare:

    predicted values
            VS
    actual values

    using appropriate evaluation procedures.

❌ Bigger problem

You said:

    "the more the data, the more accurate the prediction"

    Careful. More data does not automatically mean a more accurate model.

    This is a major engineering lesson.

    Imagine I give you:

    10 million

    records containing terrible measurements, duplicated records, systematic errors, or irrelevant features.

    You've just given the model 10 million opportunities to learn garbage. 😂

    More useful data can help.

But: More data ≠ automatically better model

We care about things like:

    - data quality
    - representativeness
    - feature quality
    - label quality
    - distribution
    - model choice
    - evaluation methodology

And later:

    - generalization
    - overfitting
    - underfitting
    - data leakage
    - distribution shift

These are going to become major concepts.