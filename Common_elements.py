a1,a2=map(int,input().split())
a=list(map(int,input().split()))[:a1]
b=list(map(int,input().split()))[:a2]
def s(lis):
    s=[]
    for i in lis:
        if i not in s:
            s.append(i)
    return s
c=[]

for i in s(a):
    if i  in s(b):
        c.append(i)


print(*c)