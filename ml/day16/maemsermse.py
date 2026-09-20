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

'''
MSE is measured in:
score-points²

That's awkward.
If your model predicts:
Score = 80

you don't want to explain its error using some strange squared unit.
That's where RMSE : Root Mean Squared Error comes in.
        Errors
        ↓
        Square them
        ↓
        Average them
        ↓
        Take the square root
        ↓
        RMSE
        
        Basically RMSE=(squareroot(MSE))
        

'''

#🧠 The important relationship between MAE,MSE,RMSE

'''
    Don't memorize three disconnected metrics.

    Understand the family:

                    Prediction Errors
                            │
                ┌──────────┴──────────┐
                ↓                     ↓
                MAE                  MSE
                │                     │
        absolute errors        squared errors
                │                     │
        proportional impact    large errors amplified
                                        │
                                        ↓
                                    √MSE
                                        │
                                    RMSE

    MAE:"How far away are my predictions on average?"

    MSE:"How much should I punish large errors?"

    RMSE:"How much error do I have, in the original target's scale, while still strongly penalizing large errors?"

    That's the conceptual progression.
'''


#⚔️ Challenge 16 — RMSE

    Do this without looking back.

    Suppose:

    Actual:     [50, 60, 70]
    Predicted:  [52, 57, 78]
    A.

    Calculate the residuals using:

    actual - predicted
    B.

    Calculate the absolute errors.

    C.

    Calculate MAE.

    D.

    Calculate the squared errors.

    E.

    Calculate MSE.

    F.

    Calculate RMSE.

    G. The important one:

    If MAE = 3.0 and RMSE = 5.2, what does the fact that RMSE is considerably larger than MAE suggest about the model's errors?

    Don't just calculate. Interpret.

    After this, we're moving into train/test split → generalization → overfitting, which is where model evaluation starts becoming genuinely practical.

'''
a.) -2,3,-8
b.) 2,3,8
c.) MAE=13/3=4.33
d.) MSE=4+9+64=77
e.) 77/3=25.67
f.) RMSE=5.07
g.) NO Idea but i could simply suggest that RMSE generalized well with MAE 

'''

#Correction on G:
'''

    correction G.
    G — The important part

    You said:

    "RMSE generalized well with MAE"

    Not quite. RMSE is not a measure of generalization.

    Generalization asks: How well does the model perform on unseen data?

    RMSE and MAE are metrics used to measure prediction error.

    Now compare:

    MAE  = 3.0
    RMSE = 5.2

    RMSE being considerably larger tells us:

    The model likely has some relatively large errors that are being heavily amplified by squaring.

    Why?

    MAE treats:

    error = 10 → 10

    MSE/RMSE treats:

    error = 10 → 100 → √100 = 10

    The key difference is that large errors contribute disproportionately to MSE, which pushes RMSE upward.

    So:

    MAE ≈ 3
    RMSE ≈ 5.2

    suggests the errors aren't all uniformly around 3. There are probably some larger deviations.

    But be precise: MAE and RMSE alone don't tell us exactly what the error distribution is. We'd inspect the individual residuals to know for sure.

    That's the kind of precision I want from you.
'''

    🚨 NOW WE CROSS AN IMPORTANT LINE

    We've learned:

    Residual
    ↓
    Absolute Error
    ↓
    MAE
    ↓
    Squared Error
    ↓
    MSE
    ↓
    Square Root
    ↓
    RMSE

    But all of these metrics answer essentially:

    "How wrong is the model?"

    We haven't properly answered:

    "Does the model actually work on students it has never seen?"

    That's generalization.

    And this is where a lot of beginners get fooled.

'''

training data → model → predictions → metric