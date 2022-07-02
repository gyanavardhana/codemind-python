s1=(input().lower())
s2=(input().lower())
c=0
for i in s1:
    if i not in s2:
        c+=1
if c==0:
    print(True)
else:
    print(False)