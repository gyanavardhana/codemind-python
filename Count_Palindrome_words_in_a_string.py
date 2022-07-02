s=input()
n=s.split()
c=0
for i in n:
    i=i.lower()
    if i==i[::-1]:
        c+=1
print(c)