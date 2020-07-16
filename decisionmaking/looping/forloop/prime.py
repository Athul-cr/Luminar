num=int(input("enter the number :: "))
flag=0
for i in range (2,num):
    if(num%i==0):
        flag=1
    else:
        pass
if(flag>0):
    print("not a prime")
else:
    print("prime")