
s=input()
a=[]
for i in range(0,len(s)):
    c=0
    for j in range(0,len(s)):
        #checking if two characters are equal
        if(s[i]==s[j] and i!=j):
            c=1
            break
    if(c==0):
        a.append(s[i])
a=sorted(a)
l=[]
for i in a:
    if ord(i)>90:
        l.append(i)
l=sorted(l)
for i in l:
    print(i,end='')