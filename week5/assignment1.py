# https://elzero.org/python-assignments-lesson-from-33-to-37/
# Operators & Type Conversion

# task 1
print(bool(True))
print(bool(10))
print(bool("Ahme)d"))
print(bool(10.5))

print(bool(False))
print(bool(0))
print(bool(""))
print(bool(False))

print("#" * 50)
# task 2
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)


print("#" * 50)
# task 3
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


print("#" * 50)
# task 4
num_one2 = 10
num_two2 = 20

result = num_one2 + num_two2
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000) / 5)
print(type(str((((result ** 3) % 26000) / 5))))