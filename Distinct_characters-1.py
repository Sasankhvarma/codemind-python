l=input()
l=l.lower()
k=[]
for i in l:
    if l.count(i)==1 and i!=' ':
        k.append(i)
k.sort()
for i in k:
    print(i,end='')