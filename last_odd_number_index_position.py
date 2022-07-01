n=int(input())
l=list(map(int,input().split()))[:n]
k=0
for i in range(n):
    if l[i]%2!=0:
        k=i
print(k)