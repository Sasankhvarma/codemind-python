n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
c=int(input())
d=0
for i in l:
    if i<=c:
        d+=1
    else:
        d+=2
print(d)