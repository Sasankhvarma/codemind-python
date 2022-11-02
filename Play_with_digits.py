def fun(n):
    s=0
    while n>0:
        s=s+n%10
        n//=10
    return s

n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+fun(i)
print(s)