n=input()
s=n.split()
for i in range(len(s)):
    s[i]=s[i][::-1]
print(*s)