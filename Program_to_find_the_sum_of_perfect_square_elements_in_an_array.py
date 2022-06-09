t=input()
l=list(map(int,input().split()))
a=[]
k=0
def sqrt(n) :
    i = 1
    while(i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True
        i = i + 1
    return False
for i in l:
    if sqrt(i):
        k=k+i
print(k)

