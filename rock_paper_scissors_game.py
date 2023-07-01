import random
user_score = 0
computer_score = 0
choice_list=["rock", "paper", "scissor"]
while True:

    user_input=input("Type rock or paper or scissor, to quit type q: ").lower()
    computer_input = random.choice(choice_list)
    if user_input=="q":
        if user_score==0:
            quit()
        else:
            print("Your score is "+str(user_score)+" and computer score is "+str(computer_score))
            if computer_score>user_score:
                print("Computer wins the game")
            elif user_score>computer_score:
                print("You win the game") 
            else:
                print("you both have same score")   
    elif user_input=="rock" and computer_input=="paper":
        print("Computer has a "+computer_input+", so computer win")
        computer_score+=1
    elif user_input=="rock" and computer_input=="scissor":   
        print("Computer has a "+computer_input+", so you win")
        user_score+=1
    elif user_input=="paper" and computer_input=="scissor":   
        print("Computer has a "+computer_input+", so computer win")
        computer_score+=1
    elif user_input=="paper" and computer_input=="rock":   
        print("Computer has a "+computer_input+", so you win")
        user_score+=1
    elif user_input=="scissor" and computer_input=="paper":   
        print("Computer has a "+computer_input+", so you win")
        
    elif user_input=="scissor" and computer_input=="rock":   
        print("Computer has a "+computer_input+", so computer win")
        computer_score+=1
    else:
        print("You both have "+computer_input+" . So tie")
        computer_score+=1
        user_score+=1
        continue
    

