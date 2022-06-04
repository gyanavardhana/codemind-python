def pal(n):
    k=str(n)
    if n==int(k[::-1]):
        return True
    else:
        return False
print(pal(int(input())))