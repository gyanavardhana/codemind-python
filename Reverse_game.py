n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    i=str(i)
    print(int(i[::-1]),end=" ")