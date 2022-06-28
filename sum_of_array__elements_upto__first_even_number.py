n=int(input())
l=list(map(int,input().split()))[:n]
su=0
for i in l:
    if i%2==0:
        break
    else:
        su+=i
print(su)