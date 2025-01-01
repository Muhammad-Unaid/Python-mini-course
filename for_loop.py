# string = text
#int = whole number
# float = decimal
# list = collection of items

# l = ['h','e','l','l','o']

# sentence = "pakistan"

# print(sentence[-2])
# for i in l:
#     print(i, end="")

# print(l[len(l)-1])

# number = l[2]
# print(number)

[0,1,2,3,4,5,6,7,8,9]

# for i in range(10):
    # print(i)



# create a list of numbers. print out the sum of the numbers in the list

# numbers = [1,2,3]
# sum = 0

# for i in numbers:
#     sum = sum+i

# for i in range(len(numbers)):
#     sum = sum + numbers[i]

# print(sum)

# create a list of numbers. print out the mean of the numbers in the list

# numbers = [1,2,3]
# sum = 0

# for i in numbers:
#     sum = sum+i

# mean = sum/len(numbers)
# print(mean)

# take a string as an input. print out each character of the string

# a = input("Enter any word: ")
# for i in a:
#     print(i)

# print out numbers from 1 to 10, but skip 5


# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)

# appending to a list

# l = [1,2,3]
# l.append(4)
# print(l)

# popping from a list

# l = [5,6,7]
# l.pop()
# print(l)

# inserting into a list

# l = [7,8,9]
# l.insert(1,11)
# print(l)

# removing from a list

# l = [7,8,9]
# l.remove(7)
# print(l)

# replacing in a list

# l = [1,2,3,4]

# position = l.index(3)
# l[position] = 5
# print(l)

# create a list. swap the first and last numbers. print the list

# l = [1,2,3,4,5]

# temp = l[0]
# l[0] = l[-1]
# l[-1] = temp

# print(l)

# reverse items in a list

# l = [1,2,3,4]
# l.reverse()
# print(l)

# sort items in a list

# l = [5,1,11,2,7]
# l.sort()
# print(l)

# exit out of a loop

# l = [1,2,3,4,5]
# for i in l:
#     if i == 3:
#         break
#     print(i)

# create an empty list. take 5 numbers as input, and store in list. print list
# l = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     l.append(num)
# print(l)

# take length of list as input from user. take inputs. find sum. find average

#printing numbers from 0 to n
# n = int(input("Enter a num: "))

start = int(input("Enter start: "))
end = int(input("Enter end: "))
skip = int(input("How many places to skip? "))
for i in range(start, end, skip):
    print(i)
