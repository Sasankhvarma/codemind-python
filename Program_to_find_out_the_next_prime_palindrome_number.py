def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def pal(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
    
    
n=int(input())
c=0
for i in range(n+1,100000):
    if i==pal(i) and prime(i):
        print(i)
        break