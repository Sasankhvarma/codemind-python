r,c=map(int,input().split())

row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
s1,s2=0,0        
for i in range(r):
    for j in range(c):
        if d[i][j]%2==0:
            s1+=d[i][j]
        else:
            s2+=d[i][j]
print(s1,s2)