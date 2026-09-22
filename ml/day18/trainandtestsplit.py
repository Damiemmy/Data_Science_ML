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

'''

              MODEL EVALUATION
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
   Does it generalize?   Is it accurate enough?
          │                   │
      Train vs Test       MAE/RMSE/etc.
'''

'''

🚀 NOW LET'S ACTUALLY SPLIT YOUR DATA

You've been calculating metrics using:

model.fit(X, y)

prediction = model.predict(X)

This is the problem.

You're training and evaluating on the same data.

We need:

X, y
 │
 ├──────────────┐
 ↓              ↓
TRAIN           TEST
 │               │
 ↓               │
fit()            │
 │               │
 └──────┐        │
        ↓        ↓
       MODEL ← TEST
          │
          ↓
      prediction
          │
          ↓
       MAE/RMSE

Scikit-learn gives us:

'''

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)
prediction = model.predict(X_test)

mae = mean_absolute_error(y_test, prediction)
rmse = np.sqrt(mean_squared_error(y_test, prediction))

print(mae)
print(rmse)

'''

How will this model actually be used?
                ↓
What will unseen data look like?
                ↓
How should I construct my test set?

'''

'''
🧠 So there are actually several different dangers

This is why I don't want you to memorize:

     test_size=0.2
     random_state=42

     without understanding the bigger picture.

     You need to ask:
     1. Did the model see the test examples?
     NO → good
     YES → evaluation is compromised

     2. Is the test set large enough?
     1 example → terrible basis
     20 examples → still potentially unstable
     10,000 representative examples → much stronger evidence

     3. Does the test set represent real-world data?
     Random split → sometimes appropriate
     Time-dependent problem → chronological split may be appropriate
     Grouped data → group-aware splitting may be necessary

     4. Did information from the future leak into the features?
     NO → good
     YES → leakage
'''

#Mental Model:
'''

                 REAL WORLD
                     │
                     ↓
          What will the model
          see after deployment?
                     │
                     ↓
          How do I simulate that
              during testing?
                     │
                     ↓
              SPLIT DATA
              /         \
             /           \
        TRAIN             TEST
          │                 │
          ↓                 ↓
      Learn from       Simulate unseen
       historical         reality
        examples           │
          │                ↓
          └──────────→ Evaluate

And now the four variables make sense:

X_train → clues the model is allowed to learn from

y_train → correct answers for those clues

X_test  → new clues the model did NOT learn from

y_test  → correct answers we use to judge its predictions

Then:

model.fit(X_train, y_train)

means:

Learn from the training examples.

And:

prediction = model.predict(X_test)

means:

Now make predictions on examples you weren't trained on.

And:

mean_absolute_error(y_test, prediction)

means:

Compare those predictions with the real answers and measure how wrong the model was.

'''

'''

Then:

model.fit(X_train, y_train)

means:

Learn from the training examples.

And:

prediction = model.predict(X_test)

means:

Now make predictions on examples you weren't trained on.

And:

mean_absolute_error(y_test, prediction)

means:

Compare those predictions with the real answers and measure how wrong the model was.

'''

'''

🎯 One final distinction

random_state controls repeatability.

test_size controls how much data you hold out.

But neither one answers the most important question:

"Did I design my evaluation to realistically measure how this model will perform in the real world?"

That's the deeper ML problem.

And honestly, that question is far more important than memorizing random_state=42.

'''

#⚔️ CHALLENGE 18 — DATA SPLITTING

'''
Now I want you to reason before coding.

Suppose we're building a system that predicts a student's final score before the final exam.

Available information:

student_id
study_hours
attendance
assignment_score
final_exam_score
final_grade

We want to predict:

final_grade

Answer:

1.

Which columns could potentially be legitimate features?

2.

Which columns should definitely NOT be used as features?

3.

Why is final_exam_score dangerous?

4.

Why is student_id probably not a useful predictive feature?

5.

Suppose:

Training MAE = 2.0
Test MAE = 2.1

Can we immediately conclude the model is ready for production?

6. Hardest:

Suppose someone says:

"Our model has a test MAE of 1.2, so it's definitely better than our old model with MAE 2.0."

What questions would you ask before accepting that conclusion?

This last question is deliberately broader. I want you to start thinking like an ML engineer rather than someone merely calculating metrics.
'''

#Answers:

'''
1. study_hours_attendance_assignment_score are the features, 2. final_exam_score and final_grade, 3. final_exam_score leaks the targets already so it might be accurate in training but fail in production, 4.) student_id doesn't contribrue to a student performance , 5.)yes we can conclude it's ready for production it the training performance and test performance generalize well  6.) i would ask what is the training performance and test performance and i would also observe if there was any data leakage involved that made the output looks accurate. please review my answer and let's add pace as they are other things we need to learn i don't want to leave anystone unturn but i want to learn very fast and be exceptionally good and dangerous that all industry would value me 
'''

#correction :

#1. Legitimate features

You chose:

study_hours
attendance
assignment_score

✅ Correct.

These could plausibly be known before the final grade is produced.

The important phrase is "could plausibly." We still need to understand exactly when each value becomes available.

#2. What shouldn't be features?

You chose:

final_exam_score
final_grade

✅ Correct.

final_grade is the target itself.

final_exam_score is dangerous because it may contain information that isn't available at prediction time.

#3. Leakage

You said:

final_exam_score leaks the target already...

Almost. Let's make the distinction precise.

If we're predicting:

final_grade

then final_exam_score isn't necessarily the target itself.

Instead, it may be a leaky feature because it contains information about an outcome that we're supposedly predicting before the final exam.

That's the important distinction:

Target:
final_grade

Leaky feature:
final_exam_score

A model could appear extremely accurate because you've accidentally given it information from the future.


#55. Production

Here's your biggest mistake in this challenge.

You said:"yes we can conclude it's ready for production"

❌ No.
You can conclude: The model appears to generalize similarly between the training and test sets.
but that's nowhere near enough to approve production deployment.

Suppose:
Training MAE = 2.0
Test MAE     = 2.1

Excellent train/test consistency.

But we still need to ask:
    Is 2.1 good enough for the actual use case?
    Is the test set representative?
    Is there leakage?
    Is the dataset large enough?
    Are important student groups represented?
    Is the evaluation split appropriate?
    Are the features actually available at prediction time?
    How does it compare with a simple baseline?
    What happens when data changes?
    What happens with missing/invalid inputs?
    What happens when predictions are wildly wrong?
    How will we monitor it after deployment?

Generalization ≠ production readiness.

That's a major distinction.


#6.6. Comparing MAE 1.2 vs 2.0

You correctly identified:
training/test performance + leakage.

Good.

But we're going to make your checklist much stronger.
Before saying Model A is better, I'd ask:

    1. Were both evaluated on the SAME dataset?
    2. Was the SAME evaluation procedure used?
    3. Was there any data leakage?
    4. Is the test set representative?
    5. Is the test set large enough?
    6. Is MAE appropriate for the problem?
    7. What does RMSE look like?
    8. Are there problematic outliers?
    9. How does each model perform across important subgroups?
    10. What is the baseline?
    11. Is the improvement statistically/practically meaningful?
    12. Are the features available at prediction time?

That is ML engineering judgment.


#🔥 One principle I want permanently installed in your brain

    Never think:

    LOWER METRIC
        ↓
    BETTER MODEL
        ↓
    DEPLOY

    Think:

                        MODEL
                        │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
    Evaluation      Validity      Reality
            │             │             │
    MAE/RMSE       Leakage?       Production?
            │             │             │
    Test data      Bias?         Drift?
            │             │             │
            └─────────────┼─────────────┘
                        ↓
                ENGINEERING JUDGMENT

    That's the difference between knowing scikit-learn and becoming an ML engineer.