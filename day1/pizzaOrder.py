#Based on a user's order, work out their final bill.

#Small Pizza: $15

#Medium Pizza: $20

#Large Pizza: $25

#Pepperoni for Small Pizza: +$2

#Pepperoni for Medium or Large Pizza: +$3

#Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

amount = 0
if size == 'S':
    amount += 15
    if add_pepperoni == 'Y':
        amount += 2
elif size == 'M':
    amount += 20
    if add_pepperoni == 'Y':
        amount += 3
else:
    amount += 25

if extra_cheese == 'Y':
    amount += 1

print(f"Your final bill is: {amount}.")
