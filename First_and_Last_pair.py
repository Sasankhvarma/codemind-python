n=int(input())
lst=list(map(int,input().split()))
a=0
b=n-1
for i in range(n):
    if i%2==0:
        print(lst[a],end=" ")
        a+=1
    else:
        print(lst[b],end=" ")
        b-=1
if n%2!=0:
    print(0,end=" ")