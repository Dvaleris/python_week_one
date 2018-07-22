# Homework Week 1, Day 2

# Full name greeting
print("First name, please:")
first_Name = input()

print("Middle name next:")
middle_Name = input()

print("Finally, your last name:")
last_Name = input()

print("Welcome, " + first_Name + " " + middle_Name + " " + last_Name + "!")

# Bigger, better favorite number

print("What is your favorite number?")
fav_Num = input()
int_Num = int(fav_Num) + 1
better_Num = str(int_Num)

print("Have you considered choosing " + better_Num + " instead? I've heard it's a bigger, better number.")

# Angry boss
print()
print("Press ENTER to continue")
input()
print("This is the Angry Boss Simulator.")
print("What do you want, " + first_Name + " " + middle_Name + " " + last_Name + "?")
response = input()

print('WHADDAYA MEAN "' + str.upper(response) + '"?!? YOU\'RE FIRED!!"')

# Table Of Contents (centered for string length = 100)
print()
print("Press ENTER to display the Table Of Contents")
input()

toc = "Table Of Contents"
chap1 = "Chapter 1: Getting Started"
chap2 = "Chapter 2: Numbers"
chap3 = "Chapter 3: Letters"

print(toc)
print()
# print(chap1 + "page 1".rjust(50-len(chap1),".") )
# print(chap2 + "page 9".rjust(50-len(chap2),"."))
# print(chap3 + "page 13".rjust(50-len(chap3),"."))

print(chap1.ljust(50,".") + "page 1")
print(chap2.ljust(50,".") + "page 9")
print(chap3.ljust(50,".") + "page 13")

# CivIII Random Grid Generator
print()
print("Press ENTER to continue to Random Grid Generator")
input()

grid_Num = 0
row_Num = 0
total = 11
tile_List = ["O", "X"]

import random

#for i in range(total):
#    print(random.randrange(0, 101,5))

tile_Type = random.choice(tile_List)

#while grid_Num <= total:
for i in range(total):
    #while row_Num <= total:

#    row_Num = row_Num + 1
    print(str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List))
    + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)) + str(random.choice(tile_List)))
    #i + i + i + i + i + i + i + i + i + i)
#row_Num = row_Num + 1
#grid_Num = grid_Num + 1
#    pass
pass
