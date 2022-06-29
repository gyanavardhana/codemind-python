n=input()
s=n.split()
a=[]
b=[]
s1=0
s2=0
for i in s:
    a.append(min(i))
    b.append(max(i))
for i in a:
    s1+=ord(i)
for i in b:
    s2+=ord(i)
print(abs(s1-s2))