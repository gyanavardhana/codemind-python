t=int(input())
l=list(map(int,input().split()))
def j(i):
    i=str(i)
    k=len(i)
    return k
c=0
for i in l:
    if j(i)%2==0:
        c=c+1
print(c)