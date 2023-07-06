n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
f=[]
for i in range(n):
    if i<len(o):
        f.append(o[i])
    if i<len(e):
        f.append(e[i])
for j in f:
    print(j,end=' ')
if n%2!=0:
    print(0)
    
    