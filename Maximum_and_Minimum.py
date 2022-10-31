n=int(input())
l1=list(map(int,input().split()))
l2=[]
l3=[]
c=0
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    if i==l1.count(i):
        l3.append(i)
        c+=1
        

if c==0:
    print("-1")
else:
    print(min(l3),max(l3))
