f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/movies.csv","r")
r=[]
m=[]
dic={}
count=0

for line in f:
    for e in range(1, 50):
    words=line.rstrip("\n").split(",")
    rate=words[3]
    r.append(rate)
    movie=words[1]
    m.append(movie)
for i in m:
    for l in r:
        if(i not in dic):
            dic[i]=r[count]
            count+=1
print(dic)
max=(max(r))
print("Highest Rating=>",max)
print("Movies With Highest Rating")
print("__________________________")
for x,y in dic.items():
     if(y==max):
         print(x)
#
#
#
