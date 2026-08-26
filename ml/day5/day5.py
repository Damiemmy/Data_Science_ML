import numpy as np
'''
Print:

shape
ndim
dtype
number of elements

Hint: NumPy has a property that tells you the total number of elements.

Don't search for it immediately. Think about what you already know.
'''
data = np.array([
    [20, 5, 90],
    [19, 7, 95],
    [21, 3, 70],
    [20, 8, 98],
    [22, 2, 65]
])
'''
Challenge 2 — Extract Features

Extract:

age
study_hours
attendance

as three separate arrays.

You already know how to do this.
'''

print(data.shape)
print(data.ndim)
print(data.dtype)
number_of_elements = np.size(data)
print("Number of elements:",number_of_elements)

ages = data[:,0]
print('Ages:',ages)

study_hours = data[:,1]
print('Study hours',study_hours)

attendance = data[:,2]
print('Attendance', attendance)

'''
Challenge 3 — Feature Statistics

Calculate:

average age
average study hours
average attendance
highest attendance
lowest attendance
'''

average_age= np.mean(ages)
print("Average Age:",average_age)

average_study_hour=np.mean(study_hours)
print("Average Study Hours:",average_study_hour)

average_attendance=np.mean(attendance)
print("Average Attendance:",average_attendance)

highest_attendance=np.max(attendance)
print("Highest Attendance:",highest_attendance)

lowest_attendance=np.min(attendance)
print("Lowest Attendance:",lowest_attendance)

'''
Challenge 4 — Filtering

This is the new concept.

Given:

attendance = [90,95,70,98,65]

find students whose attendance is at least 90.

Don't use a Python for loop.

Think about how NumPy might allow you to ask:

Which values satisfy this condition?

This introduces you to Boolean masking, one of the most useful NumPy concepts.
'''

attendance = np.array([90, 95, 70, 98, 65])

print(attendance >= 90)

print(attendance[attendance >= 90])














damisa_record=np.array([[23,34,45,67],[23,34,45,65]])

print("DAMISA:",damisa_record.shape)
print("DAMISA:",damisa_record.ndim)
print("DAMISA:",np.size(damisa_record))
print("DAMISA:",np.mean(damisa_record[0]))
print("DAMISA:",damisa_record.dtype)

print(damisa_record[0][damisa_record[0]>=34])