l=input()
l=l.lower()
m=1
for i in l:
    if l.count(i)==1:
        print(i)
        m=0
        break
if m==1:
    print(-1)