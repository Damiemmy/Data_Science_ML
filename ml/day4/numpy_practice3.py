#print array,type,shape,number of dimensions from this data [70, 80, 90, 60, 75]

import numpy as np


scores=np.array([70, 80, 90, 60, 75])

print(scores)
print(type(scores))
print(scores.shape)
print(scores.ndim)

'''
2.)
Challenge 2 — Vectorized operations

Using the same array, calculate:

+5 to every score
-10 from every score
×2 every score
÷2 every score
'''
new_score = scores + 5
print(new_score)
new_score = scores - 10
print(new_score)
new_score = scores * 2
print(new_score)
new_score = scores / 2
print(new_score)


'''
3.)
Challenge 3 — Statistics

Use NumPy to calculate:

total
mean
maximum
minimum

You'll discover functions such as:

np.sum()
np.mean()
np.max()
np.min()

Don't blindly copy them. Think about how they relate to the Python functions you've already used.

'''
total_scores=np.sum(scores)
print(total_scores)
highest_score=np.max(scores)
print(highest_score)
lowest_score=np.min(scores)
print(lowest_score)
average_score=np.mean(scores)
print(average_score)

'''
4.)
Challenge 4 — Your First Dataset Matrix

Create this NumPy array:

[
 [20, 5, 90],
 [19, 7, 95],
 [21, 3, 70],
 [20, 8, 98],
 [22, 2, 65]
]

Interpret the columns as:

age
study_hours
attendance

Then print:

shape
number of dimensions
first student
first student's age
all study hours
all attendance values

This introduces you to indexing and slicing, which will become extremely important.

'''

student_performance = np.array([
    [20, 5, 90],
    [19, 7, 95],
    [21, 3, 70],
    [20, 8, 98],
    [22, 2, 65]
])


shape=student_performance.shape
print(shape)

number_of_dimension=student_performance.ndim
print(number_of_dimension)

first_student=student_performance[0]
print(first_student)

first_student_age=student_performance[0,0]
print(first_student_age)

#for numply slice
total_study_hours=student_performance[:,1]
print("Total study hours=",total_study_hours)

total_attendance_value=student_performance[:,2]
print("Total attendance value=",total_attendance_value)



#Python attempt
#My observation: python can return numpy array list but with a format which is not practical e.g np.int64(5), np.int64(7), np.int64(3), np.int64(8), np.int64(2)]
total_study_hours=[]
for hours in student_performance:
    total_study_hours.append(hours[1])

print(total_study_hours)

all_attendance_value=[]
for hours in student_performance:
    all_attendance_value.append(hours[2])

print(all_attendance_value)