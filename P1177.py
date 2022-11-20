N=int(input())
a=input().split(' ')
list=[]
for i in range(N):
    a[i]=int(a[i])
    list.append(a[i])
list.sort(reverse=False)
for i in list:
    print(i,end=" ")
