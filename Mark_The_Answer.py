a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
k=0
for i in l:
    if i<=b:
        c=c+1
    elif i>b:
        k=k+1
        if k>1:
            break
print(c)    