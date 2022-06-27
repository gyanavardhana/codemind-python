n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
a=[]
def f(n):
    c=0
    for i in l:
        if n==i:
            c=c+1
    return c
        
for i in s:
    if f(i)==i:
        a.append(i)
su=sum(a)
if len(a)==0:
    print(-1)
else:
    print('%.2f'%(su/len(a)))