#Calculator for Fence cost
#Author: Sean Park
#Date: 2024-11-1
#Version 1


#Ask user for width and loop until they enter a number that is more than zero
def num_check(question):
    error_1 = "Please enter a number more than 0"
    error_2 = "Please enter a number"

    while True:
        try:
            response = float(input(question))

            if response and response > 0:
                return response
            else:
                print(error_1)

        except ValueError:
            print(error_2)

#Main routine goes here
keep_going = ""
while keep_going == "":
    
    #Get width and height 
    width = num_check ("width: ")
    length = num_check ("length: ")
    cost = num_check ("Cost per meter: ")

    # Calculate Area / Perimeter
    perimeter = 2 * (width + length)
    Total_cost = perimeter * cost

    #Display output
    print()
    print(f"Perimeter: {perimeter} m")
    print(f"Cost: ${Total_cost}")

    #Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit.")
    print()

print("Thank you for using the Fence cost calculator.")