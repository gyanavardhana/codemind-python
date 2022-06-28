n=int(input())
k=list(map(int,input().split()))[:n]
c=0
b=int(input())
def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True
for i in k:
    if i>=b:
        if prime(i)==True:
            c+=1
print(c)
    