n=int(input())
l=list(map(int,input().split()))

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
c=1     
for i in l1:
    if i==l.count(i):
        c=0
        print(i,end=" ")
if c==1:
    print(-1)