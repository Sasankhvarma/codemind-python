n=int(input())
l=list(map(int,input().split()))
s,c=0,0
for i in range(n):
    if l[i]==1:
        c+=1
    if l[i]==0 or i==n-1:
        if c>s:
            s=c
            c=0
print(s)