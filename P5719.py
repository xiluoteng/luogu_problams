m=input().split()
n=int(m[0])
k=int(m[1]) 
A=[] 
B=[] 
for n in range(1,n+1):
    if n%k==0:
        A.append(n)   
    else:
        B.append(n) 
asw1=sum(A)/len(A)
asw2=sum(B)/len(B) 
print('%.1f'%asw1,end=' ')
print('%.1f'%asw2,end=' ')
