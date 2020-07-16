f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/redataset/complete.csv","r")
dict={}
i=0
for line in f:
    word=line.rstrip("\n").split(",")
    print(word)
    country=word[1]
    state=int(word[4])
    if country not in dict:
        dict[country] = state
    else:
        dict[country] = state

caselist=[]
for k,v in dict.items():
    caselist.append(v)
print(sum(caselist))
