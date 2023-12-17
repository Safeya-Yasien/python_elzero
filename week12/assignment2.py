# https://elzero.org/python-assignments-lesson-from-90-to-94/
# Error Handling & Debugging

NUM = input("Add Your Number ")

# Your Code Here
if len(NUM) > 1:
    raise IndexError("Only One Character Allowed")
elif len(NUM) < 0:
    raise ValueError(f"Number Must Be Larger Than {NUM}")
elif (NUM >= 'a' and NUM <= 'z') or (NUM >= 'A' and NUM <= 'Z'):
    raise Exception("Only Numbers Allowed")
else:
    print(f"The Number is {NUM}")
    

print("*" * 50)
# task 2
LETTER = input("Add Letter From A to Z")

# Your Code Here
try:
    LETTER = input("Add Letter From A to Z")
    
    if len(LETTER) > 1:
        raise IndexError
    elif LETTER > 'A' and LETTER < 'Z':
        raise ValueError
    else:
        print(f"You Typed '{LETTER}'")
except IndexError:

    print("You Must Write One Character Only")

except ValueError:

    print("The Letter Not In A - Z")
    


print("*" * 50)
# task 3
def calculate(num1, num2) -> int:
    return num1 + num2

print(calculate(20, 30))