"""
Write a program that takes user's total working hours of the month. 
If they are greater than 75, calculate the monthly wage according 
to a rate of Rs 500 per hours, else calculate the wage according to a rate of a Rs 350 per hour

The program should continue to do this until user enters a negative value for hours
"""

hours = int(input("enter hours:"))

while hours >= 0:    
    if hours > 75:
        salary = hours * 500
    else:
        salary = hours * 350
    print(salary)

    hours = int(input("enter hours: "))    
    