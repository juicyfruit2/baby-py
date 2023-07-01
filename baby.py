# Testing if the user is 18 or older and allowed entry into a party

user = int(input("Enter the year of your birth:"))
print(user)

current_year = 2023

age = current_year - user
print(age)

if age >= 18:
    print("Congrats you are old enough")







