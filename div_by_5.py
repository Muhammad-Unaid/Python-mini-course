# Write a program that keeps asking the user to input a number and stops
# if the number entered is divisible by 5. Expected Input: 3 8 20 
# Expected Output: Stopped! 20 is divisible by 5.

n = float(input("Enter a number: "))

while n % 5 != 0:
    n = int(input("Enter a number: "))

print("Stopped!", n, "is divisible by 5")

