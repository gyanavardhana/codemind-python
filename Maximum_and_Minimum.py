n=int(input())
l=list(map(int,input().split()))[:n]
s=[]
for i in l:
    if i==l.count(i):
        s.append(i)
if len(s)==0:
    print(-1)
else:
    print(min(s),max(s))