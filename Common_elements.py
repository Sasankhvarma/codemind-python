a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]

for i in l1:
    if i not in l3:
        l3.append(i)
        
for i in l2:
    if i not in l4:
        l4.append(i)
c=0      
for i in l3:
    if i in l4:
        print(i,end=" ")
