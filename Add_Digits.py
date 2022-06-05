def sum(n):
    s=0
    while(n>0 or s>9):
        if n==0:
            n=s
            s=0
        s+=n%10
        n//=10
    return s
num=int(input())
r=sum(num)
print(r)