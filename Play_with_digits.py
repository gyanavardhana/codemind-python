n=int(input())
l=list(map(int,input().split()))[:n]
c=0
r=0
for i in l:
    while i!=0:
        c=i%10
        r=r+c
        i=i//10
print(r)
    

        
