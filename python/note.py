#1. Python Variables: 
    Python variables reference objects.
#2. types:
    str,int,float,bool,list,tuple,set,dict and NoneType
#3. What's the difference between a list and tuple?
    A strong answer:
    "Both are ordered collections, but lists are mutable while tuples are immutable. I'd use a list when the collection needs to change and a tuple when the data should remain fixed."
#4.)list and dictionaries
    students = ["John", "Mary", "David"]
    student = {
        "name": "John",
        "age": 22,
        "department": "Computer Science"
    }
#5. Conditions
    age = 20

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    #Multiple conditions:

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    else:
        grade = "C"

#5. Functions:A professional Python developer should naturally think in functions.

    Why functions? Because they give us:
        - reuse
        - organization
        - testability
        - readability
        - separation of concerns
#6.)difference between print() and return:
print() sends output to the console, while return sends a value back to the caller and terminates the current function execution.
Memorize the concept, not the sentence.

#7.)for coding test use this to return error value
raise ValueError("Score must be between 0 and 100"):