t=int(input())
l=list(map(int,input().split()))
n=int(input())
m=max(l)
for i in l:
    if i+n>=m:
        print(True,end=' ')
    else:
        print(False,end=' ')
