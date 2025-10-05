# import random
# select=("rock","paper","scissor")
# player=input("select one :")
# computer=random.choice(select)
# print(player)
# print(computer)
# if(player==computer):
#     print("draw")
# elif(player=="rock" and computer=="scissor") or \
#     (player=="paper" and computer=="rock") or \
#     (player=="scissor" and computer=="paper"):
#     print("player win")
# else:
#     print("computer win")


import random
item_list = ["Rock", "Paper", "Scissor"]
score_list = ["your_score == 0","computer_score == 0","Tie_score == 0"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice} , Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
        
