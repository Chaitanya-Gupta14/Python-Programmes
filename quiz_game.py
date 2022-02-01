print("Welcome to QUIZ GAME")
play = input("Do you Wanna Play My Game? ")
if play.lower() == "yes":
    print("Let's begin!!")
else:
    print("Thank You!")
    quit()

Score = 0
answer = input("Q1. What is the creators Name? ")
if answer.lower() == "chaitanya":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q2. What does he like to eat? ")
if answer.lower() == "italian":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q3. What is his github name? ")
if answer.lower() == "hlwa007":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q4. Which country does he live in? ")
if answer.lower() == "india":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Q5. What is he interested in? ")
if answer.lower() == "exploration":
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
