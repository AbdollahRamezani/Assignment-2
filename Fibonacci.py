n = int(input("please enter number : "))
total = 0 
x = 1 
y = 1
if n < 0 :
    n = input(" please enter positive number : ")   
if n == 0 :
    print("It's impossible")   
if n == 1  : 
    print(x)    
if n == 2 : 
    print(x)   
    print(y)
if n >= 3 :
    print("Fibonacci Series: ", end='' )
    print(x, end=' ') , print(y, end=' ')   
    for i in range(0 , n-2):  
        total = x + y
        x =y
        y = total 
        print(total, end=' ')


