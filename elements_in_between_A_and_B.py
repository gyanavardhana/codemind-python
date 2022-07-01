n=int(input())
l=list(map(int,input().split()))[:n]
a,b=map(int,input().split())
m=[]
k=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        m.append(l[i])
for i in l:
    if i not in m:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    print(*(k))