s=input()
c=0
l=len(s)
for i in range(l):
    if s[i]=='1':
        c+=1
    elif s[i]=='2':
        c+=2
    elif s[i]=='3':
        c+=3
    elif s[i]=='4':
        c+=4
    elif s[i]=='5':
        c+=5
    elif s[i]=='6':
        c+=6
    elif s[i]=='7':
        c+=7
    elif s[i]=='8':
        c+=8
    elif s[i]=='9':
        c+=9
print(c)