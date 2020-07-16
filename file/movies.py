f=open("C:/Users/pranav/PycharmProjects/firstproject/file/file/movies.csv","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(",")
    print(words)
    year=words[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
lst=[]
for k,v in dict.items():
    print((k,v))
