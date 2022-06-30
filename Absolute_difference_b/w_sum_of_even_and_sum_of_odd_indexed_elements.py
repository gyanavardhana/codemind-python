n=int(input())
l=list(map(int,input().split()))
su1,su2=0,0
for i in range(0,len(l),2):
    su1+=l[i]
for i in range(1,len(l),2):
    su2+=l[i]
print(abs(su1-su2))