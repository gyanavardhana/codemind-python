t,j,w=map(int,input().split())
l=list(map(int,input().split()))
while j!=0:
    k=l[t-1]
    l=[k]+l
    l.pop()
    j=j-1
for i in range(0,w):
    p=int(input( )) 
    print(l[p])