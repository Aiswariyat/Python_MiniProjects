print("Welcome to the Polygon Quiz")
playing = input("Do you want to play the game? ")
score=0
if playing.lower()!="yes":
    quit()

answer=input("how many sides does a triangle have(type in words)? ")
if answer.lower()=="three":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("how many sides does a rectangle have(type in words)? ")
if answer.lower()=="four":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("how many sides does a pentagon have(type in words)? ")
if answer.lower()=="five":
    print("Correct!")
    score+=1
else:
    print("Wrong Answer!")
print("Final score is : ", score)

