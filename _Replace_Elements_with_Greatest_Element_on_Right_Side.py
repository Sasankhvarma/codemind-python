n=int(input())
l=list(map(int,input().split()))
m,c=0,0
for i in range(n-1):
    c=0
    for j in range(i+1,n):
        if l[j]>c:
            c=l[j]
    print(c,end=' ')
print(-1)