def tip_calculate(bill, percentage):
    tip = bill * percentage / 100
    print(tip)

bill = float(input("Enter your bill: "))
percentage = float(input("Enter the tip percentage: "))

tip_calculate(bill, percentage)