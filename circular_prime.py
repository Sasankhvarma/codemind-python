def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
 
def pal(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    return s
   
n=int(input())
if prime(n)==1 and prime(pal(n))==1:
    print("circular prime")
elif  prime(n)==1 and prime(pal(n))!=1:
    print("prime but not a circular prime")
else:
    print("not prime")
