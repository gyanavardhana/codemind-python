t=int(input())
a=[]
for i in range(t):
    e=int(input())
    a.append(e)
k=int(input())
c=0
b=0
for i in a:
    if i<=k:
        c=c+1
    elif i>k:
        b=b+2
print(c+b)