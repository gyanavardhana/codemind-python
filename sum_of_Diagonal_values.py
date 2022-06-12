mtrx=[]
r,c=list(map(int,input().split()))
o=c
for i in range(r):
    j=list(map(int,input().split()))
    mtrx.append(j)
##to print sum of diagnols
su=0
ju=0
for i in range(r):
    for j in range(c):
        if i==j:
            su=su+mtrx[i][j]
        elif i+j==o-1:
            ju=ju+mtrx[i][j]

print(su+ju)