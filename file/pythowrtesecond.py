f=open("C:/Users/pranav/PycharmProjects/firstproject/file/names","r")
fwp=open("C:/Users/pranav/PycharmProjects/firstproject/file/passed","r")
fw=open("C:/Users/pranav/PycharmProjects/firstproject/file/out.txt","w")



def readDataFromFile(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
st1=readDataFromFile(f)
st2=readDataFromFile(fwp)
print(st1)
print(st2)
fail=st1-st2
print(fail)


