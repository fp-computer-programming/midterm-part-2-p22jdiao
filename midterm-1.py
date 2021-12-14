# Author: JD 12/14/2021

import random

def clone():
    decide = input("Name a clone?")
    decide = decide.upper()
    numli = []
    for x in range(9999):
        numli.append(x + 1)
    li = []
    while decide == "Y":
        name = random.choice(numli)
        numli.remove(name)
        name = str(name)
        if len(name) == 1:
            it = "CT-000" + name
        elif len(name) == 2:
            it = "CT-00" + name
        elif len(name) == 3:
            it = "CT-0" + name
        else:
            it = "CT-"+name
        print("New clone trooper name:", it)
        li.append(it)

        decide = input("Name a clone?")
        decide = decide.upper()

    print(li)

clone()

