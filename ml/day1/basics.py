name="peter"
print(name)
age= 1
print(name)

departments=("lis","ite","edutech")
print (departments)
print(departments[0])

book={
    "title": "Talk Like Ted",
    "author": "MCKenzy",
    "publisher": "Damisa",

}

print(book)

user = {
    "name": "Damisa",
    "age": 20,
    "is_active": True
}
print(user.get("name"))


ofure_age=14

if ofure_age>=18:
    print("ofure is an aldult")
else:
    print('she is a child')

for names in departments:
    print(f"{names} is in this department")


mofe_age=0

if mofe_age > 23:
    result="mofe is above 23 years of age"

elif mofe_age < 23:
    result="mofe is less than 23 years"

elif mofe_age == 23:
    result= "mofe is 23 years old"

elif mofe_age <= 0:
    result="invalid input"





print(result)