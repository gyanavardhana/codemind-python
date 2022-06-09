
def pal(n):
    t=str(n)
    r=int(t[::-1])
    if n==r:
        return True
    else:
        return False
n=int(input())
for i in range(1,n//2):
    if pal(n-i) and pal(n+i):
        print(n-i,n+i)
        break
    elif pal(n-i):
        print(n-i)
        break
    elif pal(n+i):
        print(n+i)
        break