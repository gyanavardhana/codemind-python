t=int(input())
a=[]
b=[]
l=list(map(int,input().split()))
for i in l:
    if i==0:
        a.append(i)
    elif i==1:
        b.append(i)
for i in b:
    a.append(i)
print(*a)