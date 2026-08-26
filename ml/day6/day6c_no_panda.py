import csv
scores=[]
with open("students_dirty.csv","r") as file:
    reader=csv.DictReader(file)
    # next(reader)

    for student in reader:
        name=student["name"]
        age=student["age"]
        score=int(student["score"])
        scores.append(score)
        print(name,age,score)
    print(scores)