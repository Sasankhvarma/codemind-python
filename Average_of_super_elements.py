n=int(input())
l=list(map(int,input().split()))
s=0
c=0
lst=[]
for i in l:
    if i not in lst:
        lst.append(i)
for i in lst:
    if i==l.count(i):
        s=s+i
        c=c+1

if c==0:
    print(-1)
else:
    m=s/c
    print('%.2f'%m)