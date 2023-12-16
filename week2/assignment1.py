# https://elzero.org/python-assignments-lesson-from-11-to-18/

# task 1
name, age, country = "Safeya", 20, "Egypt"
print(f"\"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

# task 2
print(f"\"Hello '{name}', How You Doing \\\n\"\"\" Your Age Is \"{age}\"\" +\nAnd Your Country Is: {country}")

# task 3
name2 = "Elzero"

print(name2[1])
print(name2[2])
print(name2[len(name2) - 1])

# task 4
print(name2[1:4])
print(name2[::2])
print(name2[-2::-2])

# task 5
name3 = "#@#@Elzero#@#@"
print(name3.strip("#@#@"))

# task 6
num = "9"
# num = "15"
# num = "130"
# num = "950"
# num = "1500"

print(num.zfill(4))


# task 7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# task 8
name_one1 = "OSamA"
name_two2 = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())


# task 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# task 10
name4 = "Elzero"
print(name4.index('z'))

# task 11
msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3", "Love", 1))

# task 12
msg3 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3", "Love"))


# task 13
name5 = "Osama"
age5 = 38
country5 = "Egypt"

print(f"My Name Is {name5}, And My Age Is {age5}, And My Country Is {country5}")