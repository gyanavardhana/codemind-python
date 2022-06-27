def f(n):
    c=0
    for i in l:
        if n==i:
            c=c+1
    return c
n=int(input())
l=list(map(int,input().split()))
def lis(lis):
    s=[]
    for i in lis:
        if i not in s:
            s.append(i)
    return s
a=[]
s=lis(l)
for i in s:
    if f(i)==i:
        a.append(i)
print(len(a))