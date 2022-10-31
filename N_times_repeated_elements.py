n=int(input())
l1=list(map(int,input().split()))
k=int(input())

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
c=0
for i in l2:
    if l1.count(i)==k:
        print(i,end=" ")
        c+=1
if c==0:
    print(-1)