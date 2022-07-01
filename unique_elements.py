n=int(input())
l=list(map(int,input().split()))[:n]
def s(lis):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s
print(*(s(l)))