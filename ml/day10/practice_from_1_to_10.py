import csv

scores=[]
ages=[]
names=[]

with open("students_dirty.csv","r") as file:
    reader=csv.DictReader(file)

    for student in reader:
        name=student["name"]
        age=student["age"]
        score=student["score"]
        names.append(name)
        print(name,age,score)

    age_count=sum(age)
    if age_countprint(age_count)