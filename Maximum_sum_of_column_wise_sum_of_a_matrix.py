r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
l=[]
for j in range(c):
    s=0
    for i in range(r):
        s=s+d[i][j]
    l.append(s)
print(max(l))