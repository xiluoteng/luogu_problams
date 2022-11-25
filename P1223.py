def qsort(water):
    if len(water) <= 1:
        return water
    L=[]
    E=[]
    G=[]
    P=water[0]['val']
    for i in water:
        if i['val']<P:
            L.append(i)
        elif i['val']==P:
            E.append(i)
        else:
            G.append(i)
    return qsort(L)+E+qsort(G)
n=int(input())
m=input().split()
d=[]
for i in range(n):
    d.append({})
    d[i]['val'] = int(m[i])
    d[i]['num'] = i+1
d=qsort(d)
ans=0
for i in range(n-1):
    ans+=d[i]['val']*(n-i-1)
for i in range(n):
    print(d[i]['num'],end=" ")
print("")
print("%.2f"% (ans/n))
