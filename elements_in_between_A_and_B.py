n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
k=[]
for i in l:
    if i<a or i>b:
        m.append(i)
for i in l:
    if i not in m:
        k.append(i)
if len(k)==0:
    print(-1)
else:
    
    print(*k)