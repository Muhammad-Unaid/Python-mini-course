"""
You need to write a program for a grade calculator
    - The program takes input from the user for the 
    number of exams he appeared for
    - For each exam, the program asks the user to enter
    the score he achieved in that exam    
    - Calculates the percentage of the student and the grade
    as well
        > The criteria for the grade is as follows:
            o If percentage is greater than 80, A
            o If percentage is greater than 70, B
            o If percentage is greater than 60, C
            o Else D
"""

#take input from user about how many exams he appeared in
exams_appeared = int(input("Enter the number of exams you appeared for: "))
sum = 0

counter = 0

# while counter < exams_appeared:
#     score = float(input("Enter your score: "))
#     sum += score
#     counter += 1

for i in range(exams_appeared):
    score = float(input("Enter your score: "))
    sum += score

total = exams_appeared * 100
percentage = (sum / total) * 100

if percentage > 80:
    grade = 'A'
elif percentage > 70:
    grade = 'B'
elif percentage > 60:
    grade = 'C'
else:
    grade = 'D'

print("Percentage is", percentage)
print("Grade is", grade)