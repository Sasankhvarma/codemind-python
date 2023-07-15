s=input()
k=input()
s=s.lower()
k=k.lower()
c=0
l="qwertyuiopasdfghjklzxcvbnm"
for i in l:
    if i in s and i not in k:
        c+=1
    if i in k and i not in s:
        c+=1
print(c)