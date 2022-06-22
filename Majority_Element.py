t=int(input())
l=list(map(int,input().split()))
k=t//2
for i in l:
    if l.count(i)>k:
        print(i)
        break