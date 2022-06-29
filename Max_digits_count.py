n=int(input())
l=list(map(int,input().split()))
k=len(str(max(l)))
c=0
for i in l:
    if len(str(i))==k:
        c+=1
print(c)
    