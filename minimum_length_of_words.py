s=input()
s=s.split()
min=len(s[0])
for i in s:
    if len(i)<min:
        min=len(i)
print(min)