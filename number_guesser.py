import random

playing=input("Do you want to play the game?" )

if playing.lower()!="yes":
    quit()

randomNumber= random.randint(0,10)

guess=0
while True:
    number=int(input("type a number between 1 to 10: "))
    if number==randomNumber:
        
        if guess==0:
            print("You got it correct within the first guess!")
        else:
            print("You got it and you took totally "+str(guess)+" guesses")
        break
        
    else:
        print("your guess is incorrect, try again")
        guess+=1
    
        