n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n):
    if l[i]%2==0:
        a.append(i)
for i in a:
    if i%2!=0:
        print(False)
        break
else:
    print(True)