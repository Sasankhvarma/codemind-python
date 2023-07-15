s=input()
k=input()
s=s.lower()
k=k.lower()
c=0
l="qwertyuiopasdfghjklzxcvbnm"
for i in l:
    if i in s and i in k:
        c+=1
print(c)