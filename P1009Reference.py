import math as m
a=int(input())
ans=0
for i in range(1,a+1):
   ans+=m.factorial(i)
print(ans)
