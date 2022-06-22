t=int(input())
l=list(map(int,input().split()))
def f(n):
    c=0
    for i in l:
        if n>i:
            c=c+1
    return c
for i in l:
    print(f(i),end=' ')