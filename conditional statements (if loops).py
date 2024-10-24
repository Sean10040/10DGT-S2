#Conditional statements and while loops
#Author: Sean Park
#Date: 2024-09-27
#Version 1
#TODO: Create a program that asks a user a question 
#and returns a response based on the answer of the user.


#Main loop. Keeps running until a condition is met
keep_going = ""
while keep_going == "":

    like_coffee = input("Do you like coffee?").lower()


    if  like_coffee == "yes" or like_coffee == "y":
        print("I like coffee too!")
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out!")

    like_tea = input("Would you like tea instead?").upper()
    if like_coffee == "no" or like_coffee == "n":
        print(like_tea)

        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try!")
        elif like_tea == "NO" or like_tea == "N":
            print("Tea is amazing though!")

    else: 
        print("I don't understand")

    keep_going = input("Press <enter> to continue or any key to quit")

