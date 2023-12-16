# https://elzero.org/python-assignments-lesson-from-56-to-59/
# Function

# task 1
def calculate(num1, num2, operation = "add"):
    if operation == "add" or operation == "a":
        return num1 + num2
    elif operation == "subtract" or operation == "s":
        return num1 - num2
    elif operation == "multiply" or operation == "m":
        return num1 * num2
    else:
        return "this operation not found"

num1 = int(input("enter first number: ").strip())
num2 = int(input("enter second number: ").strip())
opeartion = input("enter operation: ").strip().lower()

print(calculate(num1, num2)) # 30
print(calculate(num1, num2, opeartion)) # 30
print(calculate(num1, num2, opeartion)) # 30
print(calculate(num1, num2, opeartion)) # 30

print(calculate(num1, num2, opeartion)) # -10
print(calculate(num1, num2, opeartion)) # -10

print(calculate(num1, num2, opeartion)) # 200
print(calculate(num1, num2, opeartion)) # 200



print("*" * 50)
# task 2
def addition(*nums):
    sum = 0
    for i in nums:
        if i == 10:
            continue
        if i == 5:
            sum -= i
        else:
            sum += i
    return sum

print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160





print("*" * 50)
# task 3
def show_skills(name, *skills):

    if skills == ():
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name}")
        for i in skills:
            print(i)


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")



print("*" * 50)
# task 4
def say_hello(name = "Unkown", age = "Unkown", country = "Unkown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())







