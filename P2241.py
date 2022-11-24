x=input().split()
m=int(x[0])
n=int(x[1])
a=min(m,n)
b=max(m,n)
Tot=(a*(1+a)*b*(1+b))//4
Num=0
for i in range(1,a+1):
    Num+=(a-i+1)*(b-i+1)
print(Num,Tot-Num)
