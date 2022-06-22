m=[]
n=[]
r,c=map(int,input().split())
c=r
o=c
for i in range(r):
    j=list(map(int,input().split()))
    m.append(j)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for row in rez:
    n.append(row)
for i in n:
    print(max(i))