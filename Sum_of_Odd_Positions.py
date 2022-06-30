n=int(input())
l=list(map(int,input().split()))
su2=0
for i in range(1,len(l),2):
    su2+=l[i]
print(su2)