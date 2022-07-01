
def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return(True)
        else:
            return(False)
def count(n):
    c=1
    for i in range(1,n+1):
        if(n%i==0 and prime(i)==True):
            c=c+1
    print(c)
num=int(input())
l=count(num)