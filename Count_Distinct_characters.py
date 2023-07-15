l=input()
k=[]
l=l.lower()
for i in l:
    if i not in k and i!=' ':
        k.append(i)
k.sort()
print(len(k))