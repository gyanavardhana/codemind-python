n=int(input())
s=0
s2=n**2
while s2!=0:
    i=s2%10
    s+=i
    s2=s2//10

if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')