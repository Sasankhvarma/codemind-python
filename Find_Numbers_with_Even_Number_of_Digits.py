def fun(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c

n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if fun(i)%2==0:
        c+=1
print(c)