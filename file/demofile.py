

lst=[]
fl=open("C:/Users/pranav/PycharmProjects/firstproject/file/files","r")
for gete in fl:
    print(gete)
    lst.append(gete.rstrip("\n"))#rstrip for removing signs
print(lst)
#to uper case
for gete in fl:
    print(gete.upper())