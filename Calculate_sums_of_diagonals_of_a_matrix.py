mtrx=[]
r=int(input())
c=r
o=c
for i in range(r):
    j=list(map(int,input().split()))
    mtrx.append(j)
su=0
ju=0
for i in range(r):
    for j in range(c):
        if i==j:
            su=su+mtrx[i][j]
        elif i+j==o-1:
            ju=ju+mtrx[i][j]
if r%2!=0:
    ju=ju+mtrx[r//2][r//2]
    
print("Principal Diagonal:",su,sep="")
print("Secondary Diagonal:",ju,sep="")
