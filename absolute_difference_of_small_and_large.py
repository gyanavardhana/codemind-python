n=input()
s=n.split()
for i in s:
    print(abs(ord(max(i))-(ord(min(i)))),end=' ')