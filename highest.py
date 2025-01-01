"""
Create a program that takes n number of integer values from user
and outputs the highest value
"""

n = int(input("Enter the number of values u will use: "))
highest = 0

for i in range(n):
    number = int(input("Enter number: "))
    if number > highest:
        highest = number

print(highest)

lst = []
for i in range(n):
    number = int(input("Enter: "))
    lst.append(number)

print(max(lst))