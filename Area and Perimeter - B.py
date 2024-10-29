#Area and perimeter
#Author: Sean Park
#Date: 2024-10-30
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
    height = num_check ("Height: ")
    
    # Calculate Area / Perimeter
    area = width * height
    perimeter = 2 * (width + height)
    
    #Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    #Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit.")
    print()

print("Thank you for using the area/perimeter calculator.")