#Take both people's names and check for the number of times the letters in the word TRUE occurs. 

#Then check for the number of times the letters in the word LOVE occurs. 

#Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."

#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedName = name1 + name2
finalName = combinedName.lower()
true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']
trueCount = 0
loveCount = 0
for x in true:
    trueCount += finalName.count(x)

for y in love:
    loveCount += finalName.count(y)

score = str(trueCount) + str(loveCount)
intScore = int(score)

if intScore < 10 or intScore > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif intScore <= 50 and intScore >= 40:
    print(f"Your score is {score}, you are alright together.") 
else:
   print(f"Your score is {score}.")  
