s1=input()
s2=input()
s=s1.lower()
k=s2.lower()
s=s.split()
k=k.split()


if len(s)>len(k):
    for i in s:
        if i in k:
            print(i,end=' ')
else:
    for i in k:
        if i in s:
            print(i,end=' ')