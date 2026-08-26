import csv

scores = []
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for student in reader:
        name=student[0]
        age=student[1]
        score=int(student[2])

        print(name,age,score)

        scores.append(score)

    number_of_students=len(scores)
    total_score=sum(scores)
    average_score=total_score/number_of_students
    highest_score=max(scores)
    lowest_score=min(scores)

    if average_score >=70:
        performance="Excellent"
    else:
        performance="needs improvement"
    
    print("Number of Students:", number_of_students)
    print("Total Score:", total_score)
    print("Average Score:", average_score)
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)
    print("Performance:",performance)
    print("Number of Students:",number_of_students)

    
