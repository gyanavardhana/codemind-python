n=input()
l=list(n)
c=0
for i in l:
    if ord(i)>=97 and ord(i)<=122:
        c+=1
print(c)