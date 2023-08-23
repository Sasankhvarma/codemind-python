n=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
    if i not in l:
        l.append(i)
        c=0
for i in l:
    if l.count(i)==1 and i%2!=0:
        c+=1
print(c)