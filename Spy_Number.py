n=int(input())
s=0
p=1
while n!=0:
    i=n%10
    s+=i
    p*=i
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
    