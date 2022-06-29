n=input()
l=list(n)
c=0
for i in l:
    if ord(i)>=65 and ord(i)<=90:
        c+=1
print(c)