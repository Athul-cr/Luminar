import matplotlib.pyplot as plt
f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/redataset/complete.csv","r")
dict={}
for line in f:
    word=line.rstrip("\n").split(",")
    print(word)
    country=word[1]
    state=int(word[4])
    if state not in dict:
        dict[state]= country
    else:
        dict[state]= country
print(dict)
sortedlist=[]
for k,v in dict.items():
    sortedlist.append((v,k))
print(sortedlist)
sortedlst=sorted(sortedlist,reverse=True)
print(sortedlst)
