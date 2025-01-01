"""
Create a function for a driving test.
 
Parameters to be taken:
    - Age
    - Nationality
    - matric percentage

The user will pass the score if his/her age is greater than 18, 
nationality is Pakistani 
and matric percentage is greater than 65%. 
If any of these conditions is not met, the user fails the test

The function returns 'pass' or 'fail' and the result of the 
function is outputted in the main function
"""
age = int(input("Enter your age: "))
nationality = input("Enter nationality: ")
matric_percentage = float(input("Enter matric percentage: "))

def drive_test(age, nationality, matric_score):
    if age >= 18 and nationality == "Pakistani" and matric_score > 65:
        return 'pass'
    else:
        return 'fail'
    
# age = int(input("Enter your age: "))
# nationality = input("Enter nationality: ")
# matric_percentage = input("Enter matric percentage: ")

answer = drive_test(age, nationality, matric_percentage)
print(answer)