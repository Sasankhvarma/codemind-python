def sq(n):
    if n==1:
        return True
    for i in range(1,n//2+1):
        if i*i==n:
            return True
            break
    else:
        return False
        
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if sq(i):
        s+=i
print(s)