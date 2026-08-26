import numpy as np
'''
⚔️ DAY 5 — LEVEL 2

Your challenge now:

Using:

data

create a mask based on the attendance column.

Think carefully about this:

data[:, 2]

What does it represent?

Exactly:

attendance

So ask:

Which attendance values are >= 90?

Then use that Boolean result to filter the entire dataset.

Your final result should contain the three qualifying student rows.

Don't copy a solution.

Think about:

1. Extract attendance
2. Create condition
3. Use condition as a mask
4. Apply mask to the original data

'''

data = np.array([
    [20, 5, 90],
    [19, 7, 95],
    [21, 3, 70],
    [20, 8, 98],
    [22, 2, 65]
])

attendance=data[:,2]
print(attendance>=90)
data_with_or_above_ninthy=attendance[attendance>=90]
print("Attendance:",data_with_or_above_ninthy)

#1.)student attendance>=90
print("Data >= 90:",data[attendance>=90])


'''
🔥 Then We're Going One Level Deeper

After you've solved that, try these:

Challenge A

Find students with:

attendance >= 90
Challenge B

Find students with:

study_hours >= 5
Challenge C

Find students with:

age >= 20
Challenge D — Multiple conditions

Now find students where:

study_hours >= 5
AND
attendance >= 90

This introduces another major idea:

AND conditions
OR conditions

In NumPy you'll encounter:

&
|

rather than Python's normal:

and
or

Don't jump ahead and Google it. Try to reason about it first.

'''

#2.)students with study_hours >= 5

study_hours=data[:,1]
print(study_hours)
print("Study hours", data[study_hours >= 5])

#3 Find students with age >= 20

student_age=data[:,0]
print("Student Age",student_age)
print("Student Age",data[student_age >= 20])


#4 Challenge — Multiple conditions

'''

Now find students where:

study_hours >= 5
AND
attendance >= 90

This introduces another major idea:

AND conditions
OR conditions

In NumPy you'll encounter:

&
|

rather than Python's normal:

and
or

Don't jump ahead and Google it. Try to reason about it first.
'''

study_hours=data[:,1]
attendance=data[:,2]
print("Multiple Condition for study_hours >= 5 AND attendance >= 90:",data[(study_hours >= 5)  & (attendance >= 90)])

#5.) ⚔️ DAY 5 — LEVEL 3
'''
Use the same dataset.

Challenge E — OR

Find students where:

study_hours >= 5
OR
attendance >= 90

Don't use or.

Use NumPy's array-based approach.
'''
data = np.array([
    [20, 5, 90],
    [19, 7, 95],
    [21, 3, 70],
    [20, 8, 98],
    [22, 2, 65]
])

study_hours=data[:,1]
attendance=data[:,2]
ages=data[:,0]

study_hours_5_or_above= study_hours >= 5
attendance_90_or_above= attendance >= 90
study_hours_or_attendance_operation=data[(study_hours_5_or_above) | (attendance_90_or_above)]




print("Study_Hours: ",study_hours_5_or_above)
print("Attendance: ",attendance_90_or_above)
print("Study or Attendance: ", study_hours_or_attendance_operation)

#6.)Challenge F — NOT
'''
Now find students whose attendance is NOT at least 90.

You'll need to think about the opposite of:

attendance >= 90

Don't Google it.

Think:

If I have a Boolean mask, how can I reverse True and False
'''
attendance_less_than_90=data[attendance < 90]
print("Attendance Less Than 90:",attendance_less_than_90)


#7.)🔥 Challenge G — Combine 3 conditions
'''
Find students where:

age >= 20
AND
study_hours >= 5
AND
attendance >= 90

Your result should be based entirely on the dataset—not manually selected.
'''

students_age_20_and_above= ages >= 20
study_hours_5_and_above= study_hours >= 5
attendance_90_and_above= attendance >= 90

student_with_all_condition=data[(students_age_20_and_above) & (study_hours_5_and_above) & (attendance_90_and_above)]

print("Student With All Conditions",student_with_all_condition)


#8.)prediction Assignment: on attendance = np.array([90, 95, 70, 98, 65])
'''
A.)attendance >= 90: my predictions are [90,95,98]
B.)attendance < 90: my predictions are [65,70]
c.)(attendance >= 90) | (attendance < 70): my predictions are [65,90,95,98], 70 is excluded because the sign was no <=70 so it's only value less than 70 that would be included in this case
d.)(attendance >= 90) & (attendance < 70): my predictions are[],empty list,reasons is because and condition it's expecting a (True,True) statement on both end and not (True,False) nor (False,False)
'''