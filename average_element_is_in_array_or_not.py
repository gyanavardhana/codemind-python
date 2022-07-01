n=int(input())
l=list(map(int,input().split()))[:n]
k=sum(l)//n
if k in l:
    print(True)
else:
    print(False)