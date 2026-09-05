#1.
'''
students = [70, 80, 90]

total_students=sum(students)
number_of_student_column=(len(students))
print(total_students/number_of_student_column)
'''
#2.

students = ["John", "Mary", "David"]

students.append("emmanuel")
print(students)
stu=students[0]
students.remove(stu)
print(students)
count=1
for student in students:
    print(f"{student} {count + 1}") 

#3)student record save when age exist or doesn't exist 
student_record = {
    "name": "John",
    "department": "Computer Science"
}

# print("Student Name", student_record["name"])
print("Student Age", student_record.get("age"))

#4)student record with age
student_record = {
    "name": "John",
    "age":23,
    "department": "Computer Science"
}

# print("Student Name", student_record["name"])
print("Student Age", student_record["age"])

#4)student record with or without age(safe)
student_record = {
    "name": "John",
    "department": "Computer Science"
}

# print("Student Name", student_record["name"])
print("Student Age", student_record.get("age"))

