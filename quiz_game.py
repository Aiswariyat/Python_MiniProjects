print("Welcome to the Polygon Quiz")
playing = input("Do you want to play the game? ")
if playing.lower()!="yes":
    quit()

answer=input("how many sides does a triangle have(type in words)? ")
if answer.lower()=="three":
    print("Correct!")
else:
    print("Incorrect!")

answer=input("how many sides does a rectangle have(type in words)? ")
if answer.lower()=="four":
    print("Correct!")
else:
    print("Incorrect!")

answer=input("how many sides does a quadilateral have(type in words)? ")
if answer.lower()=="five":
    print("Correct!")
else:
    print("Wrong Answer!")

