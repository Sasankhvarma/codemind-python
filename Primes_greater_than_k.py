def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if prime(i)==1 and i>=k:
        c+=1
print(c)