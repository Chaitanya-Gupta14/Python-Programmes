print("Welcome to QUIZ GAME")
play = input("Do you Wanna Play My Game? ")
if play.lower() == "yes":
    print("Let's begin!!")
else:
    print("Thank You!")
    quit()

Score = 0
answer = input("Q1. What is the creators Name? ")
if answer.lower() == "cheenu":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q2. What is the his loves Name? ")
if answer.lower() == "ananya":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q3. What does he calls her by? ")
if answer.lower() == "pucha":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q4. What does he want to eat and love? ")
if answer.lower() == "pucha":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q5. What is their baby's name? ")
if answer.lower() == "chinya":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!") 

if Score > 3:
    print("Your Score is: ", Score)
    print("Congratulations!! You Played Well! ")
else: 
    print("Your Score is: ", Score)
    print("You Tried")