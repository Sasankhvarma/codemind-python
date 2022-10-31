n=int(input())
l=list(map(int,input().split()))

for i in l:
    print(i,end=" ")
if n%2!=0:
    print(0)