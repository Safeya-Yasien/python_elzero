# https://elzero.org/python-assignments-lesson-from-47-to-50/
# Loop While & Training

# task1
num = int(input("enter a number: ").strip())

if num < 0:
    print(f"Number {num} Is Not Larger Than 0")
else:
    while num > 1:
        num-=1
        if num == 6:
            continue
        print(f"{num}")



print("#" * 50)

# task 2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
count = 0

while i < len(friends) :
    if friends[i] == friends[i].capitalize():
        print(f"{friends[i]}")
    else:
        count+=1
    i+=1

print(f"Friends Printed And Ignored Names Count Is {count}")


print("#" * 50)

# task 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

  # Type The Code Here in One Line
  print("\n".join(skills));break


print("#" * 50)

# task 4
my_friends = []
max_friends = 4

while max_friends > 0:
    name = input("enter your name: ").strip()
    if name == name.upper():
        print("Invalid Name")
    elif name == name.lower():
        my_friends.append(name.capitalize())
        print(f"the added name is {name.capitalize()} and we convert first char to uppercase")
    elif name == name.capitalize():
        my_friends.append(name.capitalize())
        print(f"the added name is {name}")
    max_friends-=1
    print(f"there is still {max_friends} you can add")


