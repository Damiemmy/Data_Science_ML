import csv

scores=[]
ages=[]
names=[]

with open("students_dirty.csv","r") as file:
    reader=csv.DictReader(file)

    for student in reader:
        if student["name"] == "" or student["name"] == None:
            name="empty"
        else:
            name=student["name"]
            names.append(name)

        if student["age"] == "" or student["age"] is None:
            age = None
        else:
            try:
                age = int(student["age"])
                ages.append(age)
            except ValueError:
                age = "invalid"

        if student["score"] == "" or student["score"] == None:
            score=None
        else:
            score=int(student["score"])
            scores.append(score)
        
        
        print(name,age,score)
    
    number_of_valid_students=len(scores)
    total_score=sum(scores)
    average_score=total_score/number_of_valid_students
    highest_score=max(scores)
    lowest_score=min(scores)
    
    print("Number of valid scores:", number_of_valid_students)
    print("Total score:", total_score)
    print("Average score:", average_score)
    print("Highest score:", highest_score)
    print("Lowest score:", lowest_score)

    print(type(scores), type(ages))

        
