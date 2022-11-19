while True:
    hourse=int(input("please insert hourse: "))
    minute=int(input("please insert minute: "))
    while minute>59:
        print("! WARNING :  The minute must be between 0 and 59")   
        minute=int(input("please insert minute again: ")) 
    second=int(input("please insert second: "))
    while second>59:
        print("! WARNING :  The second must be between 0 and 59")   
        second=int(input("please insert second again: "))     
    seconds=(hourse*3600)+(minute*60)+second
    print("Seconds: ", seconds, "S")
    print("To exit/Repeat, please enter : exit/repeat")
    x=input()
    if x=="exit":
        break
  

    