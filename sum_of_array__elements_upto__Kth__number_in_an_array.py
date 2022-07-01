
n=int(input())
l=list(map(int,input().split()))
a=int(input())
su=0
for i in range(0,a):
    su+=l[i]
print(su)