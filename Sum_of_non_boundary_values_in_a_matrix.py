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
        if i!=0 and j!=0 and i!=r-1 and j!=c-1:
            s+=d[i][j]
print(s)