n=input()
n=int(n)
m=n
a=1
for i in range(1,m+1):
    for j in range(1,n+1):
        print('%02d'%a,end='') 
        a+=1
    n-=1
    print(' ')
