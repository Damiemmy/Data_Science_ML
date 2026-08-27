import pandas as pd

df=pd.read_csv("students_dirty.csv")

print(df)

#Challenge 1
dropped_missing_rows=df.dropna()
print("Dropped Missing Rows:",dropped_missing_rows) #they where 7 rows originally, 2 rows dropped, 5 rows remaining.

#note from lecture i was thought:
'''
You'll lose:

David
Grace

So now ask yourself:

Did we actually improve the dataset?

Maybe.

Maybe not.

If your dataset had 10 million rows and only 2 incomplete records, dropping them might be perfectly reasonable.

But if you had:

100 rows

and:

40 rows contain missing data

blindly deleting them would be much more serious.

Context matters.
'''


#CHALLENGE:
'''
Challenge 1

Try: df.dropna()
Ask:
    Which students disappeared?
    How many rows remain?

Challenge 2

Try filling missing values with zero:
    score → 0
    age → 0
Don't assume this is good practice.
We're experimenting. Observe what happens.

Challenge 3

Calculate:

    - mean score
    - mean age
before filling anything.
Then use those means to create temporary cleaned columns/data.

Challenge 4 — Compare

Create three versions:
Version A → drop missing rows
Version B → fill missing values with 0
Version C → fill numerical missing values using the column mean

Then compare:

    - number of rows
    - average age
    - average score

This is important.
You are going to see that your cleaning strategy can change the statistics of the dataset.
'''
#Challenge 2
filled_0_to_missing_rows=df["age"].fillna(0)
print(filled_0_to_missing_rows)#missing data are replace with value=0 which is not ideal and might be concidered unfair.

#challenge 3
average_score=df["score"].mean()
average_age=df["age"].mean()

print("Average Score:",average_score)
print("Average Age:",average_age)
#creating a temporary cleaned columns/data.
print("Clean Data Score:",df["score"].fillna(average_score))
print("Clean Data Age:",df["age"].fillna(average_age))

#Challenge 4 (compare):
print("Dropped",dropped_missing_rows)
print("Filled",filled_0_to_missing_rows)
print("Clean Data Score:",df["score"].fillna(average_score))
print("Clean Data Age:",df["age"].fillna(average_age))


# Challenge 4


version_a=df.dropna()
version_b=df.fillna(0)
version_c=df.copy()
version_c["age"] = version_c["age"].fillna(average_age)
version_c["score"] = version_c["score"].fillna(average_score)



#version A:
print("Length of Version A",(version_a.shape[0]))
print("Average Age",(version_a['age'].mean()))
print("Average Score",(version_a['score'].mean()))

#version B:
print("Length of Version B",(version_b.shape[0]))
print("Average Age",(version_b['age'].mean()))
print("Average Score",(version_b['score'].mean()))

#version C:
print("Length of Version c",(version_c.shape[0]))
print("Average Age",(version_c['age'].mean()))
print("Average Score",(version_c['score'].mean()))


'''
# Version A: Drop rows with missing values
version_a = df.dropna()

# Version B: Fill missing values with 0
version_b = df.fillna(0)

# Version C: Fill missing values with column means
version_c = df.copy()
version_c["score"] = version_c["score"].fillna(average_score)
version_c["age"] = version_c["age"].fillna(average_age)


print("\n--- COMPARISON ---")

print("Version A - Drop Missing Rows")
print("Rows:", len(version_a))
print("Average Age:", version_a["age"].mean())
print("Average Score:", version_a["score"].mean())

print("\nVersion B - Fill With 0")
print("Rows:", len(version_b))
print("Average Age:", version_b["age"].mean())
print("Average Score:", version_b["score"].mean())

print("\nVersion C - Fill With Mean")
print("Rows:", len(version_c))
print("Average Age:", version_c["age"].mean())
print("Average Score:", version_c["score"].mean())

'''

#question
'''
After experimenting, answer:

1.Why could fillna(0) be dangerous for age?

2.Why might filling a missing score with the mean be more reasonable than 0?

3.When might dropna() be preferable to filling missing values?

4.Can you think of a situation where the missingness itself might contain useful information?

That fourth question is particularly important.

Imagine a dataset where:

income = NaN

Does that necessarily mean:

"We don't care about income?"

Not necessarily.

Maybe the person refused to disclose it.

Maybe the system failed.

Maybe they don't have an income.

Those are three completely different situations.

And that takes us toward serious data science.

'''

#answer:
'''
1.) fillna could be dangerous for age because it might 0 representing a student or an entity age is not logical and it could change the statistic totally 
2.) filling a  missing score with the mean is more reasonable because  the average of the know value is a reasonably estimated for the missing value. 
3.) dropna is prefered when incomplete record is not relevant or useful. 
4.)base on my understanding and all you have thought me so far  in a situation when the a column name is missing this doesn't involve any statistics of calculating the known value to give a reasonable estimate for name, is not possible to maneuver to find the value,in such cases the users name column is extremely useful as it's the identity of the user before his record
'''
#correction:

'''
Your answer to Question 4

You said:if a column name is missing, statistics cannot reasonably estimate it.
You're thinking in the right direction, but let's sharpen the concept.

Suppose:

    - name
    - John
    - Mary
    - NaN
    - Sarah

You cannot calculate: mean(name)

because name isn't numerical.

But there's something even deeper:

Missingness has different meanings depending on the feature.

For example:

age = NaN

could potentially be estimated.

But: name = NaN
usually isn't something you should "guess."

And:
medical_diagnosis = NaN

would be an entirely different situation again.

So our rule becomes:
Never choose a missing-data strategy merely because Pandas gives you a function for it. Choose it based on the meaning of the data.

That's a serious principle."