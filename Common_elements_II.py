a1,a2=map(int,input().split())
a=list(map(int,input().split()))[:a1]
b=list(map(int,input().split()))[:a2]

c=[]

for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)

print(*c)