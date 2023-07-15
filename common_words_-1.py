s=input()
k=input()
s=s.lower()
k=k.lower()
s=s.split()
k=k.split()
c=0
if len(s)>len(k):
    for i in s:
        if i in k:
            c+=1
else:
    for i in k:
        if i in s:
            c+=1
print(c)