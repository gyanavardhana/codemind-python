def fact(n):
    su=0
    for i in range(1, n+1):
        if n % i == 0:
            su=su+i
    return su
l=list(map(int,input().split(',')))
a=[]
b=[]
for i in l:
    if fact(i) not in l:
        b.append(-1)
    else:
        a.append(i)
if len(l)==len(b):
    print(b[0])
else:
    a.sort()
    print(*a)
