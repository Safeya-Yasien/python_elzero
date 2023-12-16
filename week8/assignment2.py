# https://elzero.org/python-assignments-lesson-from-60-to-64/
# Packing, Recursion, Lambda


# task 1
def get_score(**subjects):
    for subject, value in subjects.items():
        print(f"{subject} => {value}")

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


print("*" * 50)
# task 2
def get_people_scores(name="", **subjects):
        if name == "":
             pass
        elif name != " " and subjects != {}:
            print(f"Hello {name} This Is Your Score Table:")
        if subjects == {} and name != "":
             print(f"Hello {name} You Have No Score Table:")
        else:
            for subject, value in subjects.items():
                print(f"{subject} => {value}")



get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")



print("*" * 50)
# task 3
scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70,
}

def get_the_scores(name="", **scores):
    if name == "":
        pass
    elif name != "" and scores != {}:
        print(f"Hello {name}, This Is Your Score Table:")
    if scores == {} and name != "":
        print(f"Hello {name} You Have No Scores To Show.")
    else:
        for subject, value in scores.items():
            print(f"{subject} => {value}")

get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)


    






































