n=int(input())
l=list(map(int,input().split()))
def s(lis):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
def f(n):
    c=0
    for i in l:
        if n==i:
            c=c+1
    return c
su=0
s=s(l)
for i in s:
    if i%2!=0:
        su+=i
print(su)