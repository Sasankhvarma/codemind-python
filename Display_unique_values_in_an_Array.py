n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if l.count(i)==1:
        print(i,end=' ')
        c+=1
if c==0:
    print(-1)