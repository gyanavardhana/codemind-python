n=input()

l=list(n)
c=0
for i in l:
    if i in '[@_!.#$%^&*()<>?/\|}{~:]':
        c+=1
print(c)