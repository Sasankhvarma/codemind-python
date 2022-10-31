n=int(input())
l1=list(map(int,input().split()))
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
c=0
for i in l2:
    if i==l1.count(i):
        c+=1
print(c)