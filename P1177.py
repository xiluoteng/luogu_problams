N=int(input())
a=input().split(' ')
list1=[]
for i in range(N):
    a[i]=int(a[i])
    list1.append(a[i])
list1.sort(reverse=False)
for i in list1:
    print(i,end=" ")
