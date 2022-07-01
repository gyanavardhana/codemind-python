n=int(input())
l=list(map(int,input().split()))[:n]
def s(lis):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
s=s(l)
s1=[]
for i in s:
    if i==l.count(i):
        s1.append(i)
print(len(s1))