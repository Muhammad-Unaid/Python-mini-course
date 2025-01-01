###function starts
def square_area(length): ###passing length as input
    area = length * length ###calculating area
    print(area) ###printing area
###function ends

###inputting length
length = float(input("Enter the length of your square: "))

###calling function and passing length as argument
square_area(length)