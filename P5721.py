n=input()
n=int(n)
m=n
a=1
for i in range(1,m+1):
    for j in range(1,n+1):
        print('%02d'%a,end='')  #n控制列数为什么print会出在这里
        a+=1
    m-=1
    print(' ')
