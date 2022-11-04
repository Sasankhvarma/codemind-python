n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    c=0
    for j in range(i,n):
        if l[j]>l[i]:
            l1.append(c)
            c=0
            break
        else:
            c+=1
        if j==n-1:
            l1.append(0)
for i in l1:
    print(i,end=' ')