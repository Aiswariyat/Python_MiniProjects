import random

playing=input("Do you want to play the game?" )

if playing.lower()!="yes":
    quit()

randomNumber= random.randint(1,10)

for i in range(0,10):
    number=int(input("type a number between 1 to 10: "))
    print(number)
    if number==randomNumber:
        print("You guessed it correctly")
        break
        
    else:
        print("your guess is incorrect, try again")
        i=i+1