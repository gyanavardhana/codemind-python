t=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if l.count(i)==1:
        a.append(i)
    else:
        c=c+1
if len(a)==0:
    print(-1)
else:
    print(max(a))