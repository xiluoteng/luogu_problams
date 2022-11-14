n=input()
n=int(n)
m=input().split()
for i in range(n):
    m[i]=int(m[i])
maxn=1001
for i in range(n):
    if m[i]<maxn:
        maxn=m[i]
print(maxn)