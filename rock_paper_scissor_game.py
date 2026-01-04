import random
item_list =["Rock", "Paper", "Scissor"]
user_choice = input("enter your move = rock, Paper , Scissor :")
computer_choice = random.choice(item_list)

print(f"user_choice={user_choice}, computer_choice={computer_choice}")
if user_choice == computer_choice:
    print("both  chooses the same move = Match Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("paper covers rock = Computer Win")
    else:
        print("Rock broke the scissor = You Win")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("scissor cuts the paper = Computer Win")
    else:
        print("paper covers the rock = You Win")
elif user_choice =="Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts the paper = You Win")
    else:
        print("Rock broke the Scissor = Computer Win")


