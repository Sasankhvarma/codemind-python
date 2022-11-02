def dig(n):
    c=0
    n=abs(n)
    if n==0:
        c=1
    while n>0:
        c+=1
        n//=10
    return c
    
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if dig(i)==k:
        c+=1
print(c)