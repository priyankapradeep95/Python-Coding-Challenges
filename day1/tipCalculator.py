#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = input("What was the total bill? ")
totalBill = float(bill) + float(bill)* 12/100
perPersonbill = round(totalBill/5, 3)
print("%.2f" % perPersonbill)
