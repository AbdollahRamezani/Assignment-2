import random
user_score=0
computer_score=0
n=int(input("Enter the number of repetitions of the Game : "))
while computer_score<n and user_score<n:
    x=random.randint(1,3)
    if x==1:
        computer_choice="rock"
    elif x==2:
        computer_choice="paper"
    elif x==3:
        computer_choice="scissor"
    user_choice=input("please insert your choice: ")

    print("computer_choice:",computer_choice)
    print("user_choice:",user_choice)

    if computer_choice=="rock" and user_choice=="paper":
        user_score=user_score+1
    elif computer_choice=="rock" and user_choice=="scissor":
        computer_score=computer_score+1
    elif computer_choice=="rock" and user_choice=="rock":
        print("Equal")

    elif computer_choice=="paper" and user_choice=="rock":
        computer_score=computer_score+1
    elif computer_choice=="paper" and user_choice=="scissor":
        user_score=user_score+1
    elif computer_choice=="paper" and user_choice=="paper":
        print("Equal")

    elif computer_choice=="scissor" and user_choice=="paper":
        computer_score=computer_score+1
    elif computer_choice=="scissor" and user_choice=="rock":
        user_score=user_score+1
    elif computer_choice=="scissor" and user_choice=="scissor":
        print("Equal") 

print("computer_score: ", computer_score)
print("user_score: ", user_score)           


