# https://elzero.org/python-assignments-lesson-from-69-to-71/
# Built In Functions

values = (0, 1, 2)

if any(values):
    # true
    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

# output "Good"


print("#" * 50)
# task 2
v = 1

while v < 1000:
    
    my_range = list(range(v))
    if (sum(my_range, v) + pow(v, v, v)) == 820:
        print(f"v's value {v}")
        break
    v+=1




print("#" * 50)
# task 3

n = 1

while n < 100:
    
    l = list(range(n))
    if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
        print("Good")
        print (f"'n' => {n}")
        break
    n+=1

# Output => Good


print("#" * 50)
# task 4

def my_all(iter):
    for i in iter:
        if not i:
            return (False)
    return (True) 
    
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False


print("#" * 50)
# task 5

def my_any(iter):
    for i in iter:
        if i:
            return (True)
    return (False)

print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False



print("#" * 50)
# task 6

def my_min(iter):
    mi = iter[0]
    for i in iter:
        if i < mi:
            mi = i
    
    return (mi)

print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100



print("#" * 50)
# task 7

def my_max(iter):
    ma = iter[0]
    for i in iter:
        if i > ma:
            ma = i
    
    return (ma)


# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700



