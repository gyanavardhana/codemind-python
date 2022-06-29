n=input()
v='AEIOUaeiou'
p=[]
for i in n:
    if i in v:
        if i not in p:
            p.append(i)
print(*p)