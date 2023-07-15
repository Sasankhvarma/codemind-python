s=input()
s=s.split()
max=len(s[0])
for i in s:
    if len(i)>max:
        max=len(i)
print(max)