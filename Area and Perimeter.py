#Calculating the Area and Perimeter in python
#Author: Sean Park
#Date: 2024-10-30
#Version 1


#Ask the user for the width and height
#Assume they put in valid data
width = float(input("Width: "))
height = float(input("Height: "))

#Calculate Area and Perimeter 
area = width * height
perimeter = 2 * (width + height)

#Output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")
