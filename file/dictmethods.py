f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/redataset/complete.csv","r")
dict={}
c=[]
s=[]
count=0
for line in f:
    word=line.rstrip("\n").split(",")
    print(word)
    country=word[1]
    c.append(country)
    state=int(word[4])
    s.append(state)