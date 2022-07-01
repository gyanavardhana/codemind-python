n=int(input())
l=list(map(int,input().split()))[:n]
m=[]
k=[]
j=n//2
for i in range(j):
    m.append(l[i])
for i in range(j,len(l)):
    k.append(l[i])
print(abs(sum(m)))
print(abs(sum(k)))