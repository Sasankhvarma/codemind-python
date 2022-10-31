n,k=map(int,input().split())
l=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    for j in range(i,n):
        s+=l[j]
        if s==k:
            c+=1
        elif s>k:
            break
    s=0
print(c)