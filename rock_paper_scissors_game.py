import random
user_score = 0
computer_score = 0
choice_list=["rock", "paper", "scissor"]
while True:

    user_input=input("Type rock or paper or scissor, to quit type q: ").lower()
    computer_input = random.choice(choice_list)
    print(computer_input)
    if user_input=="q":
        quit()
    elif user_input=="rock" and computer_input=="paper":
        print("Computer has a "+computer_input+", so computer win")
    elif user_input=="rock" and computer_input=="scissor":   
        print("Computer has a "+computer_input+", so you win")
    elif user_input=="paper" and computer_input=="scissor":   
        print("Computer has a "+computer_input+", so computer win")
    elif user_input=="paper" and computer_input=="rock":   
        print("Computer has a "+computer_input+", so you win")
    elif user_input=="scissor" and computer_input=="paper":   
        print("Computer has a "+computer_input+", so you win")
    elif user_input=="scissor" and computer_input=="rock":   
        print("Computer has a "+computer_input+", so computer win")
    else:
        print("You both have"+computer_input+" . So tie")
        continue

