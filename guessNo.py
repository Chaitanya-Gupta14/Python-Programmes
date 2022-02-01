'''
Q. Develop a guessing game which would ask the user to guess a number between a given range say 0 to 30. 
    Let the function choose a number between 0 and 30 say 18 
    and tell the user if his/her guess was right or above or below.
    Constarint is that he gets only numbered chances say 10 and
    then display the number of turns taken by the user to guess the number. 
'''
chances = 10
number = 18
i = 1
print("Hey user!! Take a guess between a number from 0 to 30. ")
while i <= chances:
    user = int(input())
    if user > 30 or user < 0:
        print("The number should be between 0 and 30!!")
        i+=1
    else:
        if user > number:
            print("Try a number BELOW")
            i+=1
        elif user < number:
            print("Try a number ABOVE")
            i+=1
        else:
            print("You found it!!")
            print("It took you",i,"chances")
            exit()
