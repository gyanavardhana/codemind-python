
def f(n):
    c=0
    for i in l:
        if n==i:
            c=c+1
    return c
n=int(input())
l=list(map(int,input().split()))
b=int(input())
def lis(lis):
    s=[]
    for i in lis:
        if i not in s:
            s.append(i)
    return s
a=[]
s=lis(l)
for i in s:
    if f(i)==b:
        a.append(i)
if len(a)==0:
    print(-1)
else:
    print(*a)