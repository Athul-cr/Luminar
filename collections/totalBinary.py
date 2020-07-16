lst=[2,5,1,4]
lst.sort()
print(lst)
low=0
upper=len(lst)-1
add=int(input("enter the number to add"))
while(low<upper):
    add=lst[low]+lst[upper]
    if(add>lst[low]):
        low=lst[low]+1

    elif(add<lst[upper]):
        upper=lst[upper]-1


