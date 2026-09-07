'''
Challenge 1

Write a function:

calculate_grade(score)

It should return:

90–100 → "A"
80–89  → "B"
70–79  → "C"
60–69  → "D"
below 60 → "F"

For example:

calculate_grade(85)

should return:

"B"

But there's another requirement:

Your function should handle an invalid score.

For example:

calculate_grade(150)

should not silently return A.

Think about what should happen.
'''

#let's kill this
def calculate_grade(score):
    if score>100 or score < 0:
        raise ValueError("Score must be between 0 and 100")
    elif score>=90:
        return ("A")
    elif score>=80:
        return("B")
    elif score>=70:
        return("C")
    elif score>=60:
        return("D")
    else:
        return("F")
    
print(calculate_grade(100))


#Challenge 2

'''

Write:

find_max(numbers)

Without using Python's built-in:

max()

Example:

find_max([4, 8, 2, 10, 5])

should return:

10
'''


def find_max(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")

    highest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number

    return highest


print(find_max([4, 8, 2, 10, 5])) # i just have to use max() lol


# #challenge 3
# '''
# Challenge 3

# Given:

# students = [
#     {"name": "John", "score": 85},
#     {"name": "Mary", "score": 72},
#     {"name": "David", "score": 91},
#     {"name": "Sarah", "score": 64}
# ]

# Write a function that returns the names of students who scored 80 or above.

# Expected:

# ["John", "David"]
# '''



#first attempt
def student_above_80(student_list):
    qualified_students=[]
    for students in student_list:
        if students["score"] >= 80:
            qualified_students.append(students["name"])
            print(qualified_students)
            return qualified_students
        else:
            raise ValueError("No Students was qualified")
    
    return qualified_students
    
#second attempt

def student_above_80(student_list):
    qualified_students=[]
    for students in student_list:
        if students["score"] >= 80:
            qualified_students.append(students["name"])
        if not qualified_students:
            raise ValueError("No Students was qualified")
    return qualified_students


students = [
    {"name": "John", "score": 90},
    {"name": "Mary", "score": 82},
    {"name": "David", "score": 70},
    {"name": "Sarah", "score": 64}
]
print(student_above_80(students))






#CORRECTION
'''

Challenge 2 😂

You said:

# i just have to use max() lol

And then:

def find_max(max_number):
    highestscore = max_number
    print(max(highestscore))

😂 You violated the assignment—but I actually like that you knew exactly what you were doing.

The problem was specifically testing whether you understand how to find the largest value yourself.

Your implementation basically does:

list → max() → answer

We need:

list → iterate → compare → keep largest → answer

Here's the thinking.

Suppose:

numbers = [4, 8, 2, 10, 5]

Start by assuming:

highest = 4

Then inspect each number:

8 > 4 → highest = 8
2 > 8 → no
10 > 8 → highest = 10
5 > 10 → no

Final:

highest = 10

That's the algorithm.

Don't copy code yet.

I want you to implement that algorithm.

'''