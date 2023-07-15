s=input()
k=input()
s=s.lower()
k=k.lower()
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in l:
    if i in s and i not in k:
        print(i,end='')
    if i in k and i not in s:
        print(i,end='')
