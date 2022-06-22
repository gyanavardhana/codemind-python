def m(l):
    return max(set(l),key=l.count)
 
t=int(input())
l = list(map(int,input().split()))

print(m(l))
