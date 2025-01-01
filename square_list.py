"""
Take size of list.
Put numbers in a list.
Create a new list in which each number is squared.
Print out both old and new lists.
"""
size = int(input("Enter size of the list: "))
old_list = []
new_list = []
for i in range(size):
    add = int(input("Enter a number: "))
    old_list.append(add)
    new_list.append(add*add)
print(old_list)
print(new_list)