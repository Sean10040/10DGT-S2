#Error checking in python
#Author: Sean Park
#Date: 2024-09-27
#Version 1


#Code that tests a valid number is entered
'''done = False #Boolean variable set to false, while loop that runs until a valid number is entered
while not done:
    num = int(input("Please enter your value:"))
    done = True

    print(f"the number you entered is {num}")'''

#Code that tests that a valid number is entered (V2)
#Create a function to call every time I ask the user for a number
#A funtion is a chunk of code that does something I can use a function
#over and over. To use a function, I 'call' it by writing out its name.
'''def test_int_num(question):
    done = False
    while not done:
        print(question) #The 'question' is a placeholder
        try:  #This tries for a valid input
            num = int(input())
            done = True

        except ValueError:
            print("That is not a valid number") 
    
    return(num) #Gives back the value of num
                #So that i can use it outside the function.
    
#main routine 
num_1 = test_int_num("Please enter your first number:")
print(f"You entered {num_1}.")

num_2 = test_int_num ("Please enter your second number:")
print(f"You entered {num_2}.")

num_3 = test_int_num ("Please enter your third number:")
print(f"You entered {num_3}.")

sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2} and {num_3} is {sum}.")'''

#Version 3. Referining my code. Making it more pythonic
# Aask the user to pick a number in a range.
def valid_num(question, low, high):
    error = f"Whoops, that is not an integer between {low} and {high}."
    while True:
        try:
            response = int(input())
            if low < response < high:
                break

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)
    return response

#Main rountine
num_1 = valid_num("Enter a number between 1 and 15: ", 1, 15)
print(f"You entered {num_1}")

num_2 = valid_num("Now enter a number between 50 and 100: ", 50, 100)
print(f"You entered {num_2}")

num_3 = valid_num("Lastly enter a number between 70 and 80: ", 70, 80)
print(f"You entered {num_3}")

#Multiply the result of num_1, num_2, num_3
multiply = num_1 * num_2 * num_3 
print(f"Your three numbers multiplied together are equal to {multiply}")
sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2} and {num_3} is {sum}.")