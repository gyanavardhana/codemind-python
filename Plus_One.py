n=int(input())
l=list(map(int,input().split()))
a=[]
j=[]
for i in l:
    a.append(str(i))
res=int("".join(a))
res=res+1
while res!=0:
    m=res%10
    j.append(m)
    res=res//10
j.reverse()
print(*j)
    