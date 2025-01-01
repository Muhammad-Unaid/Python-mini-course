"""
Program a GPA calculator for a university
The program should take the number of courses as input from the user
For each course, the user should input the credit hours and the gpa
in that course
Use this information to calculate the total semester GPA
"""

total_courses = int(input("Enter total courses: "))
sum = 0
total_CH = 0

for i in range(total_courses):
    credit_hours = int(input("Enter CH: "))
    grade = float(input("Enter grade: "))
    sum += (credit_hours * grade)
    total_CH += credit_hours

sgpa = sum / total_CH
print(sgpa)