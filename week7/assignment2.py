# https://elzero.org/python-assignments-lesson-from-51-to-55/
# Loop For & Training

# task 1
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 1
for i in my_nums:
    if i % 5 == 0:
        print(f"{count} => {i}")
        count+=1
else:
    print("All Numbers Printed")


print("#" * 50)

# task 2
for i in range(1, 21):
    if i < 10 and i not in {6, 8}:
        print(f"{str(i).zfill(2)}")
    elif i >= 10:
        print(f"{i}")
else:
    print("All Numbers Printed")


print("#" * 50)
# task 3
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

my_progress = {
    "A": 100,
    "B": 80,
    "C": 40
}

sum = 0

for i in my_ranks:
    for j in my_progress:
        if my_ranks[i] == j:
            sum += my_progress[j]
            print(f"My Rank in {i} Is A And This Equal {my_progress[j]} Points")
else:
    print(f"Total Points Is {sum}")


print("#" * 50)
# task 4

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

my_progress2 = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D": 20
}

sum = 0

for i in students:
    print("-" * 50)
    print(i)
    print("-" * 50)
    for j in students[i]:
        for p in my_progress2:
            if students[i][j] == p:
                sum += my_progress2[p]
                print(f"{j} => {my_progress2[p]} Points")
    print(f"Total Points For Mahmoud Is {sum}")
    sum = 0
            
    
    
    
    
    
    