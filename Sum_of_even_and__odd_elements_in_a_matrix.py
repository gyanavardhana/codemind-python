a,b=map(int,input().split())
mtrx=[]
for i in range(a):
    j=list(map(int,input().split()))
    mtrx.append(j)
su=0
su1=0
for i in range(a):
    for j in range(b):
        if mtrx[i][j]%2==0:
            su=su+mtrx[i][j]
        else:
            su1=su1+mtrx[i][j]
print(su,su1)