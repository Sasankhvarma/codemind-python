def fun(n):
    s=0
    while n>0:
        s=s*10+n%10
        n//=10
    return s
    
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    print(fun(i),end=' ')
                 