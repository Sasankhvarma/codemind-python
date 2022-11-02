def dig(n):
    c=0
    n=abs(n)
    if n==0:
        c=1
    while n>0:
        c+=1
        n//=10
    return c
    
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    print(dig(i),end=' ')