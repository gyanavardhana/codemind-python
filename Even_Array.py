n=int(input())
l=list(map(int,input().split()))[:n]
c=0
for i in l:
    if i%2!=0:
        c+=1
if c==0:
    print(True)
else:
    print(False)