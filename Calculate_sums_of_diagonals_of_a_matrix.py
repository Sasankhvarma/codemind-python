n=int(input())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
s1,s2=0,0
for i in range(n):
    for j in range(n):
        if i==j:
            s1+=l[i][j]
        if i+j==n-1:
            s2+=l[i][j]
print("Principal Diagonal:",end="")
print(s1)
print("Secondary Diagonal:",end='')
print(s2)