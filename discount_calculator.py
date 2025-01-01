"""
Write a function to calculate the discount for a customer and 
return bill after discount

How to calculate discount?
for bill > 10000, discount = 50%
for bill > 5000, discount = 25%
for bills less than or equal to 5000, discount = 0%
"""

bill = float(input("Enter your bill: "))

def discount(bill):
    if bill > 10000:
        disc = 0.5 * bill
        final_bill = bill - disc

    elif bill > 5000:
        disc = 0.25 * bill
        final_bill = bill - disc

    else:
        final_bill = bill

    return final_bill


bill_after_discount = discount(bill)
print(bill_after_discount)
        
        