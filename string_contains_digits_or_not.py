t=int(input())
def co(va):
    for ch in va:
        if ch.isdigit():
            return True
    return False
for i in range(t):
    s=input()
    if co(s):
        print('Yes')
    else:
        print('No')