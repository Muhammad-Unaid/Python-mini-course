"""
Take num of students in class as input

For each student, input their marks and
calculate class average
"""

n = int(input("Enter total number of students: "))
sum = 0

for i in range(n):
    marks = int(input("Enter marks of student: "))
    sum += marks

percentage = (sum / (n * 100)) * 100

print("Percentage is " + str(percentage) + '%')