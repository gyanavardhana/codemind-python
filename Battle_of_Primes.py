n1=int(input())
n2=int(input())
c=n1+n2
def prime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True
for i in range(1,34):
    if prime(c+i):
        print(i)
        break