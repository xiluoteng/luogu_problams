a=b=c=d=0
flag=False
lis1=[]
lis2=[]
lis3=[]
lis4=[]
while 1:
    s=input().strip()
    for i in s:
        if i=='E':
            lis1.append(a)
            lis2.append(b)
            lis3.append(c)
            lis4.append(d)
            flag=True
            break
        elif i=='W':
            a+=1
            c+=1
        else:
            b+=1
            d+=1
        if (a>=11 and a-b>=2) or (b>=11 and b-a>=2):
            lis1.append(a)
            lis2.append(b)
            a=b=0
        if (c>=21 and c-d>=2) or (d>=21 and d-c>=2):
            lis3.append(c)
            lis4.append(d)
            c=d=0
    if flag:
        break
for i in range(len(lis1)):
    print("%d:%d"%(lis1[i],lis2[i]))
print("")
for i in range(len(lis3)):
    print("%d:%d"%(lis3[i],lis4[i]))
