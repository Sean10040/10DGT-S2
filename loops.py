# Making loops in python
# Author: Sean Park
# Date: 20 September 2024
# Version: 1


# for loops. Repeat for a set number of times.
for name_of_loop in range(8): #The number that goes inside the bracket after range is the amount of times its going to loop
    print("Yay")

for name_of_loop in range(2):
    print("Hello")

# While loop. Runs until a condition is met or no longer is met
keep_going = "" # Empty Variable
while keep_going == "":
    print("Looping")
    print("Still looping")

    keep_going = input("Again? Or press any other key to quit")
