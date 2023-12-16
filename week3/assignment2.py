# https://elzero.org/python-assignments-lesson-from-21-to-23/

# task 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends.pop(0))

print(friends[-1])
print(friends[len(friends) - 1])
print(friends.pop(-1))

print("\nTask 2\n")
# task 2
friends2 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends2[::2])
print(friends2[1::2])



print("\nTask 3\n")
# task 3
friends3 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends3[1:len(friends3) - 1])
print(friends3[-2::])



print("\nTask 4\n")
# task 4
friends4 = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends4[-1] = "Elzero"
friends4[-2] = "Elzero"
print(friends4)


print("\nTask 5\n")
# task 5
friends5 = ["Osama", "Ahmed", "Sayed"]
friends5.append("Jack")
print(friends5)
friends5.insert(0, "Mostafa")
print(friends5)



print("\nTask 6\n")
# task 6
friends6 = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends6.pop(0)
friends6.pop(0)
print(friends6)

friends6.pop(-1)
print(friends6)


print("\nTask 7\n")
# task 7
friends7 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends7.extend(employees)
friends7.extend(school)
print(friends7)


print("\nTask 8\n")
# task 8
friends8 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends8.sort()
print(friends8)
friends8.sort(reverse=True)
print(friends8)




print("\nTask 9\n")
# task 9
friends9 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends9))


print("\nTask 10\n")
# task 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[len(technologies) - 1][0])
print(technologies[len(technologies) - 1][-1])


