import os
from collections import Counter

a=open("commonlogformat.txt","r")
b=open("ip-date.txt","w+")
for i in a:
    list1=i.split(' ')
    tmp1=list1[3]
    list2=tmp1.split(':')
    list2.pop(-1)
    c=':'.join(list2)
    b.write(list1[0])
    b.write(c)
    b.write(' ')
b.close()
a.close()

d=open("ip-date.txt","r")
e=open("ketquathongke.txt","w+")

for k in d:
    list3=k.split(' ')

f=Counter(list3)
f=str(f)
f=f.replace('Counter({','')
f=f.replace('})','')
f=f.replace(', ','\n')
e.write(f)











