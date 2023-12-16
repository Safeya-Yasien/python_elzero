# https://elzero.org/python-assignments-lesson-from-86-to-89/
# Collection Of Modules

# task 1
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  # Write Your Code Here
  my_data.append("".join(list(data)))
  final_string = "".join(my_data)

print(my_data)
print(final_string.capitalize()) # Elzero



print("*" * 50)

# task 2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  # Write Your Code Here
    if str(item1).isdigit():
        continue
    else:
        my_data.append(item1)
    
    final_string = "".join(my_data).capitalize()
    
    
print(final_string)
# print(final_string)



print("*" * 50)
# task 3
from PIL import Image

myImage = Image.open("S:\ML\python\week12\elzero-pillow.png")
# myImage.show()

myBox = (400, 0, 800, 400)
myNewImage = myImage.crop(myBox)
# myNewImage.show()

myConnverted = myNewImage.convert("L")
# myConnverted.show()
# myConnverted.save("grayscale_image.jpg")


secondRowBox = (0, 400, 1200, 800)
secondRow = myImage.crop(secondRowBox)
# secondRow.show()
rotated = secondRow.rotate(180)
# rotated.show()
connvertRotated = rotated.convert("L")
connvertRotated.show()



print("*" * 50)
# task 4

def say_hello_to(name):
  '''This function say hello to person'''
  return f"Hello {name}"

print(say_hello_to("Safeya"))

print(say_hello_to.__doc__)
help(say_hello_to)


print("*" * 50)
# task 5
"""This file contain hello function
to say hello for anyone"""
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:
    '''this function say hello to person'''
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)





























