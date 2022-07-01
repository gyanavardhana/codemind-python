n=int(input())
l=list(map(int,input().split()))[:n]
k=int(input())
if k in l:
    print(True)
else:
    print(False)