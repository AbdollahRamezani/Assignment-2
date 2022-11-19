import math
sum_corse_number=0
counter_corse=0
while True:
    choice=input("please enter your choice : ")
    test_digit=choice.isdigit()

    if  test_digit==True:
        corse_number=float(choice)
        sum_corse_number=sum_corse_number+corse_number
        counter_corse=counter_corse+1
        average=sum_corse_number/counter_corse

    if choice=="average":
            print("your average : ", average)
    elif choice=="exit":  
            break
    
    
    
    
    
   
        
        
  
    
