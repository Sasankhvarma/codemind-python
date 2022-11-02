def dig(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c
    
n=int(input())
l=list(map(int,input().split()))
l.sort()
c=0
for i in l:
    if dig(i)==dig(l[n-1]):
        c+=1
print(c)