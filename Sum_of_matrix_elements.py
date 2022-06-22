r=int(input())
c=int(input())
mtrx=[]
for i in range(r):
    j=list(map(int,input().split()))
    mtrx.append(j)
su=0
for i in range(r):
    for j in range(c):
        su=su+mtrx[i][j]
print(su)