'''
⚔️ CHALLENGE 1 — NEAREST EXAMPLE

Look at the existing students.

Which student looks most similar to:

study_hours = 6
attendance = 92

You might find:

5 hours, 90 attendance → 75
7 hours, 95 attendance → 82

The new student sits somewhere between them.

Could the predicted score reasonably be somewhere around:

75–82

?

Explain your reasoning.
'''
import pandas as pd

data = {
    "study_hours": [2, 3, 5, 7, 8],
    "attendance": [65, 70, 90, 95, 98],
    "score": [55, 70, 75, 82, 91]
}

df = pd.DataFrame(data)

print(df)
#6 study hours
#92 attendance

#Challenge 1:
'''Could the predicted score reasonably be somewhere around:
75–82

?

Explain your reasoning.
'''
yes the study hours could be found between 75-82 because of where our given values reside 6 hours comes after 5 and  before 7,and 92 comes after 90 and before 95,  6 hours and 92 attendance falls under the 4th column in between the 3rd and the 5th so that's why our target is ranging from 75-82

#Challenge 2:
79 reasons it ranges between 75-82 so i just picked the middle number, but on a second thought 92 attendance is closer to 90 than 95 so it's not actually in the middle so i would minus 1 from 79 
so my final answer or prediction for challenge 2 is 78

#Challenge 3: Identify X and Y

"x " is feature that would be looked at why "y" is the target that is to be predicted, it would be unreasonable to include target among the feature as this a seperate layers the machine learning algorithm need to look at to find relationships between both layers
x= study_hours and attendance while 
y= score which is the target


#challenge 4
'''
⚔️ CHALLENGE 4 — THE REAL QUESTION

Suppose I give you:

100 students

Then:

10,000 students

Then:

10 million students

Would manually creating rules like:

if study_hours >= ...

still be practical?

Why?

This should lead you naturally toward the reason ML exists.
'''

No it's not practical as it's time consuming and exhausting, this is why Machine Learning should exist to be able to perform and predict huge dataset with or without features


#Challenge 5:
'''
🔥 CHALLENGE 5 — PREDICT BEFORE TRAINING

Your ultimate task today:

Given:

study_hours = 6
attendance = 92

write:

predicted_score = ???

Your number.

I don't care if your prediction isn't perfect.

I care about whether you can explain:

Why did I choose this number based on the evidence?

That's the beginning of predictive modeling.
'''
i choose 79 based on the given explanation on challenge 2 above, that was my prediction reasons
