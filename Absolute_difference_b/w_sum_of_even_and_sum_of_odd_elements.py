n=int(input())
l=list(map(int,input().split()))
su1,su2=0,0
for i in l:
    if i%2==0:
        su1+=i
    else:
        su2+=i
print(abs(su1-su2))