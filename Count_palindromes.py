def pal(n):
    t=str(n)
    r=int(t[::-1])
    if n==r:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i):
        c+=1
print(c)