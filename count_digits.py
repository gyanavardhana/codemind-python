n=int(input())
l=list(map(int,input().split()))
for i in l:
    print(len(str(abs(i))),end=' ')
