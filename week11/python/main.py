import my_mod

my_mod.say_hello("Safeya")
my_mod.say_welcome("Safeya")



print("*" * 50)
# task 3
from my_mod import say_welcome
say_welcome("Safeya")


print("*" * 50)
# task 4

from my_mod import say_welcome as new_welcome
new_welcome("Safeya")




