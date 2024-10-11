num=0
while(num<9):
    print("hello world!")
    num=num+1
    
num2=1
while(num2<=9):
    if(num2==4):
        num2+=1
        continue
    elif(num2==7):
        break
    print(num2)
    num2+=1