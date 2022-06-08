t=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i not in b and a.count(i)>1:
        b.append(i)
for i in a:
    if i not in b:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)