s=input()
k=input()
s=s.lower()
k=k.lower()
c=1
l="abcdefghijklmnopqrstuvwxyz"
for i in l:
    if i in s and i in k:
        print(i,end='')
        c=0
if c==1:
    print(-1)
