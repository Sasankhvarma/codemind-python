n=int(input())
lst=list(map(int,input().split()))
l=[]

for i in lst:
    if i not in l:
        l.append(i)
s=0
for i in l:
        s=s+i
print(s)