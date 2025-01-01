"""
Ask user for size of list.
Put numbers in the list.
Add the numbers which are on even index position.
Print the sum.
"""
numbers = []
ans = 0
size = int(input("Enter size of list: "))
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append(num)
    if i%2==0:
        ans+= num

print(numbers)
print(ans)