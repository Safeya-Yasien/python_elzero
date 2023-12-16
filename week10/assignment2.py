# https://elzero.org/python-assignments-lesson-from-72-to-75/
# Map, Filter, Reduce

# task 1
def remove_chars(string):
    return (string[1: len(string) - 1])
    
    
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned_list = map(remove_chars, friends_map)
for i in cleaned_list:
    print(i)

    
print("using lambda function")
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
for i in map(lambda name: (name[1: len(name) - 1]), friends_map):
    print(i)



print("*" * 50)
# task 2

def get_names(name):
    if name.endswith("m"):
        return (name)


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)
for i in names:
    print(i)


print("using lambda function")
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
for i in filter(lambda name: name.endswith("m"), friends_filter):
    print(i)
    

print("*" * 50)
# task 3
from functools import reduce

def mult(num1, num2):
    return num1 * num2

nums = [2, 4, 6, 2]
res = reduce(mult, nums)
res = reduce(lambda x, y: x * y, nums)
print(res)
    


print("*" * 50)
# task 4

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills = reversed(skills)

counterSkills = enumerate(skills, 50)
for counter, skill in counterSkills:
    if str(skill).isnumeric():
        continue
    else:
        print(f"{counter} - {skill}")














































