x=int(input())
b=[]
while x!=0:
    a=x%10
    b.append(a)
    x=x//10
print(max(b))