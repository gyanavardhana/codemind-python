n=input()
k=n.split()
c=0
for i in k:
    l=len(i)
    if i[0] in 'aeiouAEIOU' and i[len(i)-1] not in 'aeiouAEIOU':
        c+=1
print(c)