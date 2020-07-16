num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if (num1>num2) & (num1>num3):
    if (num2>num3):
        print("number two is the second largest")
    else:
        print("number three is the second largest")
if (num2>num1) & (num2>num3):
    if (num1>num3):
        print("number number 1 is the seond largest")
    else:
        print("number three is the second largest")
if (num3>num1) & (num3>num2):
    if (num3):
        print("number three is the seond largest")
    else:
        print("invalid")
else:
    print("imvalid")

