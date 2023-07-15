k=input()
l=[]
k=k.lower()
for i in k:
    if i not in l and i!=' ':
        l.append(i)
l.sort()
for i in l:
    print(i,end='')