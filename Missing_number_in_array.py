t=int(input())
while t!=0:
    j=int(input())
    lst=list(map(int,input().split()))
    for i in range(1,j+1):
        if i not in lst:
            print(i)
    t=t-1