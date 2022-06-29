s=input()
e=input()
j=list(s)
def f(e):
    for i in range(len(j)):
        if j[i]==e:
            k=i
            return True
    if e not in j:
        return False

if f(e):
    print(f(e))
    print(j.index(e))
else:
    print(f(e))
    
       