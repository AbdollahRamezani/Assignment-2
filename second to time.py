hourse=00
minute=00
second=00
while True:
    seconds=int(input("please insert Seconds: "))
    hourse=int(seconds/3600) 
    minute=int((seconds-(hourse*3600))/60)
    second=seconds-((minute*60)+(hourse*3600))
    print ("Time:",hourse,":",minute,":",second)   


