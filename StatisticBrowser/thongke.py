import os

a=open("gistfile1.txt","r")   # doc file log
b=open("thongke.txt","w+")    # tao file thong ke de ghi 
for i in a:
    list1=i.split('"')        # tach chuoi thanh list1
    tmp1=list1[5]             # tmp1 co gia tri bang phan tu thu 5 trong list1
    list2=tmp1.split(') ')    # tach chuoi tmp1 thanh list2
    tmp2=list2[-1]            # tmp2 co gia tri bang phan tu cuoi cung trong list2
    list3=tmp2.split('/')     # tach chuoi tmp2 thanh list3
    tmp3=list3[0]             # tmp3 co gia tri bang phan tu dau tien trong list3
    b.write(tmp3)             
    b.write(' ')
b.close()
a.close()

c=open("thongke.txt","r")
d=open("ketquathongke.txt","w+")
for k in c:
    list4=k.split(' ')              # tach chuoi thanh list4

a=list4.count("Chrome")             # dem phan tu co gia tri "Chrome" trong list4
b=list4.count("coc_coc_browser")    # dem phan tu co gia tri "coc_coc_browser" trong list4
c=list4.count("Gecko")              # dem phan tu co gia tri "Gecko" trong list4

# dem tong so luot truy cap 
total=0
e=open("gistfile1.txt","r")
for line in e:
    total+=1
e.close()

# thong ke luot truy cap va ghi vao file ketquathongke.txt
d.write("Tong so luot truy cap la " + str(total) + "\n")
d.write("So luot truy cap su dung Chrome la " + str(a) + "\n")
d.write("So luot truy cap su dung Coc Coc la " + str(b) + "\n")
d.write("So luot truy cap su dung FireFox la " + str(c) + "\n")












