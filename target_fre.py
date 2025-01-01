"""
Create a list.
Ask for a target number from user.
Print the repetition of that number in the list.
"""
numbers = [1,2,3,5,1,6,1]
target = int(input("Enter a number: "))
count = 0
for i in numbers:
    if i==target:
        count = count+1

print(count)

