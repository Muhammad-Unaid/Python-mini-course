"""
Take a number as input from the user

Write a function that takes a number as a parameter and returns
1 if the number is divisible by 4 and 0 if it is not
"""

"""
Take a number as input from user

Write a function that returns whether the number is positive or negative
"""

def div_by_four(num):
    remainder = num % 4
    if remainder == 0:
        return 1
    else:
        return 0
    
def pos_neg(num):
    if num >= 0:
        return "positive"
    else:
        return "negative"
    

num1 = 34
num2 = -9

print(div_by_four(num1))
print(pos_neg(num2))