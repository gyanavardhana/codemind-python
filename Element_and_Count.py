n=int(input())
l=list(map(int,input().split()))
def f(n):
    c=0
    for i in l:
        if i==n:
            c+=1
    return c
def s(lis):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
s=s(l)
for i in s:
    print(i,f(i),end=" ")