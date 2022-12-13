r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
s=0      
for i in range(r):
    for j in range(c):
        if i==r-1 or j==c-1 or i==0 or j==0:
            s+=d[i][j]
print(s)