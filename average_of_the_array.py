n=int(input())
l=list(map(int,input().split()))[:n]
print('%.2f' % (sum(l)/n))