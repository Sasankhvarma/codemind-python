n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=max(l)
c=0
for i in l:
    if i+k>=s:
        print("True",end=' ')
    else:
        print("False",end=' ')