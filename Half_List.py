t=int(input())
l=list(map(int,input().split()))
j=t/2
b=[]
c=0
for i in range(len(l),0,-1):
    c=c+1
    b.append(l[i-1])
    if c>j-1:
        break   
##b.reverse()
for i in l:
    if i not in b:
        b.append(i)
print(*b)
