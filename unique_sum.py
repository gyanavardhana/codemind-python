n=int(input())
l=list(map(int,input().split()))

def lis(lis):
    s=[]
    for i in lis:
        if i not in s:
            s.append(i)
    return s
a=[]
s=lis(l)
print(sum(s))