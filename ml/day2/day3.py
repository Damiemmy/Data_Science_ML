import csv

scores=[]
ages=[]
names=[]
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    next(reader)

    for students in reader:
        name=students["name"]
        age=students["age"]
        score=int(students["score"])

        scores.append(score)
        ages.append(age)
        names.append(name)

    print(names,ages,scores)

    total_score=sum(scores)
    number_of_students=len(scores)
    average_scores=total_score/number_of_students
    highest_score=max(scores)
    lowest_score=min(scores)

    print(total_score,number_of_students,average_scores,highest_score,lowest_score)
    