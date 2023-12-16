# https://elzero.org/python-assignments-lesson-from-41-to-46/
# Control Flow

# task 1
num1 = int(input("enter first number: ").strip())
num2 = int(input("enter second number: ").strip())
operation = input("enter opeartion: ").strip()

if operation == "+":
    print(f"{num1} {operation} {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} {operation} {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} {operation} {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} {operation} {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} {operation} {num2} = {num1 % num2}")


print("#" * 50)
# taks 2
age = 17
print("App Is Suitable For Yo") if age > 16 else print("App Is Not Suitable For Yo")



print("#" * 50)
# taks 3
age2 = int(input("Enter your age: ").strip())

if (age2 > 10 and age2 < 100):
    months = age2 * 12
    weeks = age2 * 52
    days = age2 * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In Weeks Is {weeks} Weeks")
    print(f"Your Age In Days Is {days} Days")
    print(f"Your Age In Hours Is {hours} Hours")
    print(f"Your Age In Minutes Is {minutes} Minutes")
    print(f"Your Age In Seconds Is {seconds} Seconds")
else:
    print("age out of range")




print("#" * 50)
# taks 4
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30


if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")




