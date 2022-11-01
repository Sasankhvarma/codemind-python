n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
lst=[]
for i in l:
    if i>=a and i<=b:
        lst.append(i)
if len(lst)==0:
    print(-1)
else:
    for i in lst:
        print(i,end=" ")