#Turkish Ai Hub Introduction to Python Programming course
#Homework 2
#User Identification Program
#Student Name: Mete Çeşmeci
user = []
print("Enter information about you.")
user.append(input("First name: ").upper())
user.append(input("Last name: ").upper())
user.append(int(input("Age: ")))
user.append(int(input("Date of birth(year only): ")))

for i in user:
    print(i)

if user[2] < 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")

