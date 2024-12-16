import random
list = ["rock" , "paper" , "scissor"]
Comp_choice = random.choice(list)
User_choice = input("Choose rock , paper , scissor : ")
if User_choice == Comp_choice :
    print("Draw")
elif User_choice  == "rock" and Comp_choice == "scissor":
    print("You win")
elif User_choice == "paper" and Comp_choice == "rock" :
    print("You win")
elif User_choice =="scissor" and Comp_choice == "paper":
    print("You win")
else:
    print("You loose")