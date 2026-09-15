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

#Challenge 1:
'''
⚔️ CHALLENGE 1 — NO CODE

I don't want you touching Python yet.

Suppose the model learned:

score = 4 × study_hours + 0.5 × attendance + 1

For:

study_hours = 6
attendance = 92

What score would the model predict?

Do the mathematics manually.

Then answer:

1.

What are 4, 0.5, and 1?

2.

Which one represents the effect associated with study_hours?

3.

Which one represents the effect associated with attendance?

4.

What would happen to the prediction if attendance increased from 92 to 93, while everything else stayed the same?

Don't just give me numbers.

Explain your reasoning.
'''

the model would predict =71

1.) 4,0.5 and 1 are the mathematical relationships between the data
2.) 4 represent the associate with study_hours
3.) 1 represent the effect associate with attendance
4.) the effect associate with attendance will change


#Challenge 2:

'''

⚔️ CHALLENGE 2 — THE BIG CONCEPT

Consider:

X = df[["study_hours", "attendance"]]
y = df["score"]

Answer these without looking anything up:
A.

Why do we put:

study_hours
attendance

inside X?

B.

Why isn't score inside X?

C.

What exactly is y representing?

D.

Imagine we accidentally wrote:

X = df[["study_hours", "attendance", "score"]]

What conceptual problem have we created?

Don't worry about whether Scikit-learn throws an error.

I want the machine-learning reasoning.
'''

1. we put attendance and study_hours inside X because they are features that the machine what to understand it's mathematical relationship

2. we cant include score to X because is impractical to add the target with the features,
3. y is the target the features are pointing to and what the maching learning model is trying to predict
4. wrong predictions or missing targets depending if it's not included in y but only X but if its included in both the prediction would be totally wrong


#Challenge 3:
'''
⚔️ CHALLENGE 3 — THE MOST IMPORTANT ONE

This is where we're going to start separating you from someone who merely knows ML syntax.

Suppose you have:

Student A:
study_hours = 2
attendance = 65
score = 55

Student B:
study_hours = 8
attendance = 98
score = 91

Now you create:

Student C:
study_hours = 5
attendance = 90

We don't know C's score.

A beginner might say:

"Student C is between A and B, so estimate the score."

But machine learning asks a different question:

"What relationship between the input variables and the target can we infer from the available examples?"

Explain the difference between these two ways of thinking.
'''
the first thought is coming from a developer working on assumption while the second is objective trying to understand the mathematical relationship between input variables and the targets and knowing if it can infer or understand the relationship from the examples
