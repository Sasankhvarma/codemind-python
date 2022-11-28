n=int(input())
l=list(map(int,input().split()))
k=0
e,o=0,0
for i in l:
    if k==0:
        e+=i
        k=1
    else:
        o+=i
        k=0
if abs(e-o)==0:
    print("YES")
else:
    print("NO")