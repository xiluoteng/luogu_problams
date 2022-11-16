m=input().split()
n=int(m[0])
x=m[1]
j=[]
for i in range(1,n+1):
    j.extend(list(str(i)))
print(j.count(x))
