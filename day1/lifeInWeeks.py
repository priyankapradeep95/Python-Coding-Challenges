#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

lifeTime = 90
lifeBalance = lifeTime - int(age)
days = lifeBalance * 365
weeks = lifeBalance * 52
months = lifeBalance * 12

print (f"You have {days} days, {weeks} weeks, and {months} months left.")
