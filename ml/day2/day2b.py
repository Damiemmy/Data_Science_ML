import csv

scores=[]

with open("students.csv","r") as file:
    '''
    reader=csv.reader(file)  #for List and not use for dictionary
    '''
    reader=csv.DictReader(file) # for dictionary
    #next(reader)  : used when "csv.reader" is used,it function is To Skip header which is the first line e.g name,age,score buts using csv.DictReader does this automatically for us

    for student in reader:
        #this is for dictionary when using "reader=csv.reader(file)":
        #variable but be retrieved in this format e.g name=student[0],student[1] e.t.c"
        name=student["name"] 
        age=student["age"]
        score=int(student["score"]) 
        scores.append(score)
        print(name,age,score)

    number_of_students=len(scores)
    total_score=sum(scores)
    average_score=total_score/number_of_students
    highest_score=max(scores)
    lowest_score=min(scores)

    if average_score >=70:
        performance="Excellent"

    else:
        performance="need improvement"

    print("Number of Students:", number_of_students)
    print("Total Score:", total_score)
    print("Average Score:", average_score)
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)
    print("Performance:",performance)
    print("Number of Students:",number_of_students)