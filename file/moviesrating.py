f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/movies.csv","r")
dict={}
count=0
r=0
m=0
for lines in f:
    words=lines.rstrip("\n").split(",")
    print(words)
    rating=words[3]
    r.append(rating)
    movies=words[1]
    m.append(movies)
for i in m:
    for j in r:
        if i not in dict:
            dict[i]=r[count]
            count+=1
print(dict)
max=(max(r))
print("highest rating",max)


