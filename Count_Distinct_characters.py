s=input()
a=[]
b=[]
c=0
d=[]
n=s.split()
for i in s:
    for j in i:
        a.append(j)
for i in a:
    if i!=' ' or ord(i)>90:
        b.append(i)
b=list(set(b))
for i in b:
    if ord(i)>=65 and ord(i)<=90:
        d.append(i)
for i in b:
    if i not in d:
        c+=1
print(c)