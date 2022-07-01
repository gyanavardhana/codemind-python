n=int(input())
l=list(map(int,input().split()))[:n]
def lis(lis):
    s=[]
    for i in lis:
        if i not in s:
            s.append(i)
    return s
s=lis(l)
for i in s:
    print(i,l.count(i),end=' ')