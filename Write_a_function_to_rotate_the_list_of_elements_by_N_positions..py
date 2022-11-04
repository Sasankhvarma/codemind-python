n=int(input())
l=list(map(int,input().split()))
k=int(input())
if k>n:
    k=k%n
l1=[]
for i in range(n-k,n):
    l1.append(l[i])
for i in range(n-k):
    l1.append(l[i])
    
for i in l1:
    print(i,end=' ')