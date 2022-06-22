t=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    k=abs(i**2)
    j.append(k)
print(*(sorted(j)))