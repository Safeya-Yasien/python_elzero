# https://elzero.org/python-assignments-lesson-from-26-to-32/
# Set, Dictionary & Methods

# task 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
my_list = list(unique_list)
print(my_list)
print(type(my_list))
my_list.pop()
print(my_list)


print("\n")
print("*" * 50)

# task 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)


print("\n")
print("*" * 50)

# task 3
my_set2 = {1, 2, 3}
letters2 = {"A", "B", "C"}

print(my_set2)
my_set2.clear()
print(my_set2)
my_set2.add("A")
my_set2.add("B")
print(my_set2)
print(my_set2.discard("C"))


print("\n")
print("*" * 50)


# task 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))


print("\n")
print("*" * 50)


# task 5
myDict = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}

myDict.update({"AI": "20%"})

print(f"HTML Progress Is {myDict["HTML"]}")
print(f"CSS Progress Is {myDict["CSS"]}")
print(f"Python Progress Is {myDict["Python"]}")
print(f"AI Progress Is {myDict["AI"]}")

print()


