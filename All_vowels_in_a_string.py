s=input()
j=list(s)
j=list(set(s))

s1=['a','e','i','o','u']
s2=['A','E','I','O','U']
s3=0
s4=0
for i in j:
    if i in s1:
        s3+=1
for i in j:
    if i in s2:
        s4+=1
if s3==5 or s4==5:
    print("True")
else:
    print("False")
    