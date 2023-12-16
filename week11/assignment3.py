# https://elzero.org/python-assignments-lesson-from-81-to-85/
# Generators & Decorators


# task1
def reverse_string(my_string):
  # Your Code Here
  for i in reversed(my_string):
      yield i

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)
  
  
  
print("*" * 50)
# task 2
# Create Your Decorator Here

def myDecorator(func):
    def drink():
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)
    return drink


@myDecorator
def make_tea():
  print("Tea Created")

@myDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()



































  
  
  
  
  
  
  
  
  