f=open("C:/Users/pranav/PycharmProjects/firstproject/file\person.txt","r")


def Check(**kwargs):
    global f
    for data in f:
        data=data.rstrip("/n")


