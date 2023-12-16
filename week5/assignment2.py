# https://elzero.org/python-assignments-lesson-from-38-to-40/
# User Input & Practice

# task 1
name = input("what's your name: ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

print("#" * 50)

# task 2
age = int(input("enter your age: "))
if age < 16:
    print(f"Hello Your Age Is Under {age}, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


print("#" * 50)

# task 3
fName = input("Enter your first name: ").strip().capitalize()
lName = input("Enter your last name: ").strip().capitalize()
print(f"Hello {fName} {lName:.1s}.")

print("#" * 50)

# task 4
email = input("enter you email: ").strip().lower()
print(f"Your Name Is {email[ : email.index("@")].capitalize()}")
print(f"Email Service Provider Is {email[email.index("@") + 1: email.index(".")] }")
print(f"Email Service Provider Is {email[email.index(".") + 1: ] }")

