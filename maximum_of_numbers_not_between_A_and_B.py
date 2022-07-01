n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in l:
    if i<a or i>b:
        m.append(i)

if len(m)==0:
    print(-1)
else:
    
    print(max(m))