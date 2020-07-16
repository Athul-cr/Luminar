lst=[1,2,3,4,5,6,7,8,9]
odd=[]
even=[]
for Lst in lst:
    odd.append(Lst**Lst)
    even.append(Lst**Lst)
print("oddd",odd)
print("even",even)