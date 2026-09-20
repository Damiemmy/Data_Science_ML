import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
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
absolute_error=mean_absolute_error(y, prediction)
rmse = np.sqrt(mean_squared_error(y, prediction))

print("MAE:", absolute_error)
print("RMSE:", rmse)


#🔥 Generalization

This is one of the most important concepts in machine learning.

Generalization = the model's ability to perform well on new, unseen data.

A model doesn't become valuable because it memorized its training data.


We want:

TRAINING DATA
     ↓
learn patterns
     ↓
MODEL
     ↓
NEW DATA
     ↓
use learned patterns
     ↓
good predictions

That's learning.


'''
⚠️ OVERFITTING

Imagine:

Training MAE = 0.2
Test MAE     = 8.5

At first glance:

"Wow! MAE 0.2!"

No.

Look at the test performance.

The model performs extremely well on the data it saw, but poorly on unseen data.

That's a classic sign of overfitting.

The model has learned the training data too specifically instead of learning patterns that transfer well.

Think:

                MODEL
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
   Training data        New data
      AMAZING             BAD
        │                   │
        └──── OVERFITTING ──┘
'''

'''

⚠️ Underfitting

The opposite can happen.

Training MAE = 8
Test MAE     = 9

The model isn't doing particularly well even on the training data.

It may be too simple or unable to capture important relationships.

That's a potential sign of underfitting.

So we're looking for a model that learns useful patterns without simply memorizing the training examples.

'''

'''
⚔️ Challenge 17 — No code yet

I want pure reasoning.

We have two models:

Model A
Training MAE = 1.2
Test MAE     = 1.5
Model B
Training MAE = 0.2
Test MAE     = 7.8

Answer:

1. Which model shows the larger train/test gap?

2. Which model shows stronger evidence of overfitting?

3. Why can Model B's 0.2 training MAE actually be misleading?

4. If we care about predicting scores for future students, why should we care much more about test performance than simply looking at training performance?

5. One final engineering question:

Suppose Model C has:

Training MAE = 3
Test MAE     = 3.2

Is that automatically a perfect model?

Don't say yes/no only. Explain what you would investigate next.

After this, we're going directly into data splitting in scikit-learn, random state, validation sets, leakage, and why a single train/test split isn't the whole story.
'''
1.)model B has the larger trained/test gap
2.)model B it learn training data well enough but did not generalize well with on seen data
3.)model B can be misleading because it only understand examples but did not learn valuable patterns well enough to make predictions on new data
4.)it is a crux to care much about test performance would tell if the model learn enough pattern to make good prediction on new data

5.)no it's not a perfect model this is underfitting in disguise,it didn't capture enough data to learn patterns enough, even if the test performance is close to the training performance it's crucial that the model gets enough training example to learn from in order to perform well.

let's move to the next with full pace we have no time on our side


#Correction:

'''
5. Model C — here's your important mistake

You said:

"this is underfitting in disguise"

Not necessarily.

This is where I want you to become more careful.

Training MAE = 3
Test MAE     = 3.2

The tiny gap:

3.2 - 3 = 0.2

tells us the model's performance is fairly consistent between training and test.

That is not evidence of overfitting.

But it also does not prove the model is good.

It could be:

Good generalization + good performance

or:

Good generalization + mediocre performance

For example, if the best practically achievable MAE is around 3, that's potentially useful.

But if the problem requires MAE < 1, then 3.2 is inadequate.

So:

Generalization and predictive quality are separate questions.

You need both.

This is an important engineering principle:

              MODEL EVALUATION
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
   Does it generalize?   Is it accurate enough?
          │                   │
      Train vs Test       MAE/RMSE/etc.

Overall: ~8.5/10.

Your intuition is developing quickly. The biggest thing to eliminate now is jumping from one metric pattern to a conclusion without enough evidence.
'''