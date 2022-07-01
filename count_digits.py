n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    print(len(str(abs(i))),end=' ')