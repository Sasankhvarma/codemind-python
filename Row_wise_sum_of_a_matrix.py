r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
for i in range(r):
    s=0
    for j in range(c):
        s=s+d[i][j]
    print(s,end=' ')