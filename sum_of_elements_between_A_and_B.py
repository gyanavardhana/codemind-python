n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
k=[]
for i in l:
    if i<a or i>b:
        m.append(i)
for i in l:
    if i not in m:
        k.append(i)
print(sum(k))