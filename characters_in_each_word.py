def frq(str):
    k=[]
    str1=str.split()
    u=str1
    for words in u:
        k.append(len(words))
    print(*k)
str=input()
frq(str)