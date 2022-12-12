n=int(input())
l=list(map(int,input().split()))
k,x,y=0,0,0
for i in l:
    if k==0:
        x+=i
        k=1
    elif k==1:
        y+=i
        k=0
if abs(x-y)%4==0:
    print("X")
else:
    print("Y")