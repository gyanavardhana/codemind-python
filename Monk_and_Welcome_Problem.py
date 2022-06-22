t=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
k=[]
for i in range(t):
    c=l1[i]+l2[i]
    k.append(c)
print(*k)