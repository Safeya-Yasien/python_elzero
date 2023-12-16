# https://elzero.org/python-assignments-lesson-from-24-to-25/

# task 1
t1 = "Ahmed",
print(t1)
print(type(t1))


print("\n")
# task 2
friends = ("Osama", "Ahmed", "Sayed")
l = list(friends)
l[0] = "Elzero"
friends = tuple(l)
print(friends)
print(type(friends))
print(len(friends))



print("\n")
# task 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
c = nums + letters
print(c)
print(len(c))


print("\n")
# task 4
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)