n=int(input())
l=list(map(int,input().split()))[:n]
l1=sorted(l)
l1=l1[::-1]
if l1==l:
    print("yes")
else:
    print("no")