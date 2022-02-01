import random

#Generating Random number using:

#1. randrange() function
random.randrange(0, 10) 
#Generates random number between -5 (included) and 10 (not included)

#2. randitn() function
random.randint(0, 10)
#Generates random number between -5 (included) and 10 (included)

end = input("Emter a Number: ")

if end.isdigit():
    end = int(end)
    if end <= 0:
        print("Please enter a number more than 0 next time!")
        quit()
else: 
    print("Please Enter a Number Next Time")
    quit()

r = random.randint(0, end)
guesses = 0
while True:
    guesses += 1
    guess = input("Take a Guess!! ")
    if guess.isdigit():
        guess = int(guess)
    else: 
        print("Please Enter a Number Next Time")
        continue
    if guess == r:
        print("You Got it Right!")
        quit()
    else:
        print("Wrong answer!")

