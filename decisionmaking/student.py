name=input("enter the name of the student")
mark1=int(input("enter the mark1"))
mark2=int(input("enter the mark2"))
mark3=int(input("enter the mark3"))
sum = mark1 + mark2 +mark3
if (sum > 140 & sum <150):
    print("A+")
elif (sum >= 140 & sum < 120):
    print("b+")
else:
    print("po")