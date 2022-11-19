import random
computer_number=random.randint(1, 10)
counter=0
for i in range(10):

    user_number=int(input("please insert your number"))
    counter=counter+1    
    if computer_number>user_number:
        print("Go Up")
    elif computer_number<user_number:
        print("Go Down") 
    elif computer_number==user_number:
        print("your guess : ", counter)
        print("*** You Win ***")    
        break   
