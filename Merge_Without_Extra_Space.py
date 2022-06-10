t=int(input())
while t!=0:
    l1,l2=map(int,input().split())
    l11=list(map(int,input().split()))
    l22=list(map(int,input().split()))
    for i in l22:
        l11.append(i)
    l11.sort()
    print(*l11)
    t=t-1