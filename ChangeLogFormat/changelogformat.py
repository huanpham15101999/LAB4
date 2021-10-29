import os

a=open("access.log","r")
b=open("ketqua.txt","w+")
for i in a:
    list1=i.split('"')
    list1.pop(6)
    list1.pop(5)
    list1.pop(4)
    list1.pop(3)
    c=''.join(list1)
    b.write(c)
    b.write("\n")
