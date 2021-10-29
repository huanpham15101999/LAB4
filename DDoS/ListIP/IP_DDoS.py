import datetime

def str2datetime(str):
    return datetime.datetime.strptime(str,'%d/%b/%Y:%H:%M:%S')  # chuyen string thanh datetime

list = []                       # khoi tao list rong
a = open('access.log','r')      # mo file log
line = a.readlines()            # doc tung dong
ip = line[0].split(' ')[0]      # lay ip dong dau tien
start = str2datetime(line[0].split(' ')[3].split('[')[1]) 
end = start + datetime.timedelta(seconds=60)        
count=1

for i in range (1,len(line)):
    if ip in line[i]:           # kiem tra ip  
        time_request = str2datetime(line[i].split(' ')[3].split('[')[1])    # lay time_request
        if time_request < end: 
            count += 1
            if count > 120 and ip not in list:  # neu vuot qua 120 request/phut thi dua ip vao list 
                list.append(ip)
        else:
            start = end
            end = end + datetime.timedelta(seconds=60)
            count=1
    else:
        ip=line[i].split(' ')[0]
        start= str2datetime(line[i].split(' ')[3].split('[')[1])
        end = start + datetime.timedelta(seconds=60)
        count = 1

b = open('IP_DDoS.txt','w+')
b.write('List IP get > 120 request trong 1 phut:'+'\n')
b.write(str(list))
b.close()
a.close()

