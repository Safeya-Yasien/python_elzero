# https://elzero.org/python-assignments-lesson-from-65-to-68/
# Files Handling

# task 1
import os
# directory = "python"t
# parent_dir = "S:\ML\python\week9"
# path = os.path.join(parent_dir, directory)

# os.mkdir(path)
# print("directory created is: ", directory)

# new_file = open(r"S:\ML\python\week9\python\assign.py", "w")

for i in range(1, 51):
    if i == 25:
        new_file = "special-text.txt" 
        path = os.path.join("S:\ML\python\week9\python", new_file)
        text = open(path, "w")
    else:
        new_file = f"txt{i}.txt"
        path = os.path.join("S:\ML\python\week9\python", new_file)
        text = open(path, "w")
        text.write(f"Elzero Web School => {i}")

    

print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.basename(os.path.abspath(__file__)))


abs_path = "S:\ML\python\week9\python"
count = 0
for item in os.listdir(abs_path):
    item_path = os.path.join(abs_path, item)
    if os.path.isfile(item_path):
        count += 1

print(count)

t1 = open(r"S:\ML\python\week9\python\txt1.txt", "a")
print(t1.write("\n"))
print(t1.write("Appended => Elzero Web School\n" * 50))



t1 = open(r"S:\ML\python\week9\python\txt1.txt", "r")
print(len(t1.readlines()))
# will appears if you only comment previous line
print(len(t1.read().split()))
print(len(t1.read().replace(" ", "").replace("\n", "")))
print(t1.read().count("l"))





import os
for i in range(50, 40, -1):
    f_name = f"txt{i}.txt"
    fpath = r"S:\ML\python\week9\python"
    file_path = os.path.join(fpath, f_name)
    os.remove(file_path)

























