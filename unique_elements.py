n=int(input())
l=list(map(int,input().split()))
def f(l):
    k=[]
    for i in l:
        if i not in k:
            k.append(i)
    return k
print(*(f(l)))