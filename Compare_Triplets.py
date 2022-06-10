a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
c1=0
c2=0
for i in range(0,len(a)):
    if a[i]>b[i]:
        c1=c1+1
    elif a[i]<b[i]:
        c2=c2+1
c.append(c1)
c.append(c2)
print(*c)
