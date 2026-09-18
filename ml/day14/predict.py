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

#continuation from day 13

predictions = model.predict(X)

print(predictions)

print(f"\n#MAKING PREDICTIONS.....:\n{y}\n {predictions}")


#⚔️ CHALLENGE 7 — OBSERVATION
'''
⚔️ CHALLENGE 7 — OBSERVATION

After running it, answer:

1.

What is the difference between:

y

and:

predictions

?

2.

Are the predictions exactly equal to the original scores?

3.

If they're different, what does that difference represent?

4.

Suppose:

actual = 75
predicted = 78

How would you describe the model's error?

Don't look up an ML metric yet.

I want you to reason about the raw difference yourself.
'''


#my output on the terminal was 
'''
#MAKING PREDICTIONS.....:
0    55
1    70
2    75
3    82
4    91
Name: score, dtype: int64
 [59.52857739 64.68822139 73.87553887 84.76081213 90.14685023]

'''
1.)so the difference wasn't clear enough it's +4,-6,-2,+2,-1 so i am basically confused
2.)the predictions are not equal to the original score
3.)i think the difference represent the range between the actual and predicted score
4.)probably describes as "actual prediction increases by 3 error"

#⚔️ CHALLENGE 8 — DON'T LET ME TRICK YOU
'''
Imagine we train two models.

Model A
Training performance: 99%
Test performance: 60%
Model B
Training performance: 90%
Test performance: 88%

Without declaring either model "better" overall, explain:

What does this tell you about how each model behaves on data it hasn't seen?

And what question would you ask before deciding which model is appropriate for a real application?
'''
model A might drop missing record which it does not see "dropna" or assign it to be null
model B might have missing record but fills the data after understanding it "fillna" e.g filling missing scores with the average of the column records of a feature.

the question i would ask is what data is missing, why are they missing, could they be any better means to replace the missing data to improve prediction?


#Correction for challenge 7:
1.)The distinction is :
Actual outcome
      ↓
      y

Model's estimate
      ↓
 predictions

3.)the difference between the actual score(y) and the predicted score(prediction(X)) is called the prediction error or residual, depending on the convention being used.

4.)4. Actual = 75, predicted = 78

    You said: "actual prediction increases by 3 error"

    Not quite.

    The model predicted:

    78

    but reality was:

    75

    "So the prediction differs from reality by:"

    75 - 78 = -3

    or, if we're talking about the magnitude of the error:

    |75 - 78| = 3

    So you could say:

    "The model overpredicted by 3 points."

    That's much more precise.


    #🧠 VERY IMPORTANT DISTINCTION
    '''
    There are three things I want you to separate in your head:

    ACTUAL
    ↓
    75

    PREDICTED
    ↓
    78

    ERROR
    ↓
    3 points

    But the direction matters too:

    actual - predicted = -3

    means the model predicted too high.

    Whereas:

    actual - predicted = +3

    means the model predicted too low.

    This will matter enormously when we get into evaluation metrics.
    '''