r=int(input())

row=[0 for i in range(r)]
d1=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(r):
        d1[i][j]=val[j]
        
row=[0 for i in range(r)]
d2=[row.copy() for i in range(r)]

for i in range(r):
    val=list(map(int,input().split()))
    for j in range(r):
        d2[i][j]=val[j]
row=[0 for i in range(r)]
d3=[row.copy() for i in range(r)]        

for i in range(r):
    for j in range(r):
        d3[i][j]=abs(d1[i][j]-d2[i][j])
        
for i in d3:
    print(*i)