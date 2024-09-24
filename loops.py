# Making loops in python
# Author: Sean Park
# Date: 25 September 2024
# Version: 2
# TODO:
    #Get user input (Ask the user for their name)
    #Ask the user for 2 numbers
    #Add the numbers together

# Ask the user for their name 
name = input ("What is your name?")
print(f"Kia ora {name}.") #F stands for format. We are formatting the print

#Ask the user for two numbers
num_1 = int(input("What is your favourite number?"))
num_2 = int(input("What is your least favourite number?"))

#Add numbers together
sum = num_1 + num_2
print(f"The number added together equals to {sum}")


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
