n=int(input())
l=list(map(int,input().split()))
su2=0
for i in l:
    if i%2==0:
        su2+=i
print(su2)