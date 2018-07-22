# Week 1, Day 4 Homework

# 99 Bottles Of Beer

beer_Num = 99

while beer_Num > 2:
    print(str(beer_Num) + " bottles of beer on the wall, " + str(beer_Num) + " bottles of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, " + str(next_beer_Num) + " bottles of beer on the wall!")
    beer_Num = next_beer_Num

if beer_Num == 2:
    print(str(beer_Num) + " bottles of beer on the wall, " + str(beer_Num) + " bottles of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, " + str(next_beer_Num) + " bottle of beer on the wall!")
    beer_Num = next_beer_Num

if beer_Num == 1:
    print(str(beer_Num) + " bottle of beer on the wall, " + str(beer_Num) + " bottle of beer!")
    next_beer_Num = beer_Num - 1
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    beer_Num = next_beer_Num

# Deaf Grandma Stage 1

print()
print("Say hello to Deaf Grandma!")

import random

grandkid_Says = input()
all_Caps = grandkid_Says.isupper()
#escape_Clause = str(BYE)
rando_Year = random.randint(1930, 1951)

while grandkid_Says != "BYE":
    if all_Caps == False:
        print("HUH?! SPEAK UP, SONNY!")
    else:
        print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
    print()
    print("Say hello to Deaf Grandma!")
    grandkid_Says = input()
    all_Caps = grandkid_Says.isupper()

print("BYE! SEE YOU SOON!")

# Deaf Grandma Stage 2

print()
print("Say hello to Deaf Grandma Stage 2!")

import random

grandkid_Says = input()
all_Caps = grandkid_Says.isupper()
count = 1

while count < 3:
    if grandkid_Says == "BYE":
        print("NO, NO, STAY!")
        print()
        print("Say hello to Deaf Grandma!")
        grandkid_Says = input()
        all_Caps = grandkid_Says.isupper()
        count = count + 1
    else:
        count = 1
        if all_Caps == False:
            print("HUH?! SPEAK UP, SONNY!")
        else:
            print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
        print()
        print("Say hello to Deaf Grandma!")
        grandkid_Says = input()
        all_Caps = grandkid_Says.isupper()

print("I LOVE *nSYNC! SEE YOU SOON!")
