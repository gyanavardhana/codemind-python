def frq(str):
    k=[]
    str1=str.split()
    u=set(str1)
    for words in u:
        k.append(len(words))
    print(min(k))
str=input()
frq(str)