n=int(input())
l=list(map(int,input().split()))[:n]
m=max(l)
c=0
for i in l:
    if len(str(i))==len(str(m)):
        c+=1
print(c)