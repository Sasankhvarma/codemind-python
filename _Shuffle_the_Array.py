n=int(input())
l=list(map(int,input().split()))
s=int(input())

for i in range(s):
    print(l[i],l[i+s],end=' ')