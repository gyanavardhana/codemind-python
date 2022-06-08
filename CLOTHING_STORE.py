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
su=0
for i in b:
    k=a.count(i)
    su=su+k//2
print(su)