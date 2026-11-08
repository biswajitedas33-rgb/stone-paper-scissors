import random  


choices = ["rock" , "paper" , "scissors"]
computer = random.choice(choices)
user = input("enter rock , paper , scissors :").lower()
print("computer chose :" , computer)

if user == computer :
    print("It is tie !")
elif user=="rock":
    if computer == "scissor":
        print("YOU WON!")
    else :
        print("YOU LOSE")
elif user == "scissor":
    if computer == "rock":
        print("YOU WON!")
    else :
        print("YOU LOSE")
elif user == "scissor":
    if computer =="paper":
        print("YOU WON!")
    else:
        print("YOU LOSE!")
else :
    print("INVALID INPUT ! PLEASE CHOOSE Rock , Paper , Scissor.")
