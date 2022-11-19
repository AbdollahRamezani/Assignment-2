import random
print("*** To start Game press S & to exit Game press E ***")
x=input("insert your choice : ")

while True:
    if x=="e":
       break 
    if x!="s" and "e":
        x=input("Please enter the correct word again : ")
    if x=="s":
        dice=random.randint(1,6)
        if dice!=6:
          print(dice)
          print("!!! You Lost !!!")  
          break
        else:
            print("*** You Win ***")
            input("please Choose again : ")
           
      
   



   