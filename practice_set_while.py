# sum = 0
# number = int(input("Enter a number: "))

# while number != 0:
#     sum = sum + number
#     number = int(input("Enter another number: "))
# print(sum)

# Write a program that takes inputs from user 
#runs until user inputs 0 or sum > 50
sum = 0
# print_true = False
number = int(input("Enter a number: "))
sum = sum + number

while number != 0 and sum <= 50:
    number = int(input("Enter another number: "))
    sum = sum + number
    # print_true = True

print(sum)

# if print_true == True:
#     print(sum)
# else:
#     print("You need to enter more values")



