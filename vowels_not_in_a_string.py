n=input()
v='aeiou'
p=[]
k=[]
for i in n:
    if i in v:
        if i not in p:
            p.append(i)
for i in v:
    if i not in p:
        k.append(i)
if len(k)==0:
    print(0)
else:
    print(*k)