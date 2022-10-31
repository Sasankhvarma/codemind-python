n=input()
co=0
c=0
a='aeiou'
for i in range(0,len(n)):
    if n[i] in a:
        c+=1
    else:
        if c>co:
            co=c
            c=0
if c>co:
    co=c
print(co)