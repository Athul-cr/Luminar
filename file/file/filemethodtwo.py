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
for i in s:
    for j in c:
        if i not in dict:
            dict[i]=c[count]
            count+=1
print(dict)
max=(max(c))
print("",max)
for x,y in dict.items():
    if(y==max):
        print(x)