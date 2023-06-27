import random

playing=input("Do you want to play the game?" )

if playing.lower()!="yes":
    quit()

randomNumber= random.randint(0,10)

while True:
    number=int(input("type a number between 1 to 10: "))
    if number==randomNumber:
        print("You guessed it correctly")
        break
        
    else:
        print("your guess is incorrect, try again")
        