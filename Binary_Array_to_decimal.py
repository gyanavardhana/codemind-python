n=int(input())
l=list(map(int,input().split()))[:n]
s=0
for i in l:
    s=s*10+i
s=str(s)
k=int(s,2)
print(k)