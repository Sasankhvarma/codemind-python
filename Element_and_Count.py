n=int(input())
lst=list(map(int,input().split()))
l=[]

for i in lst:
    if i not in l:
        l.append(i)
for i in l:
    print(i,lst.count(i),end=" ")