n=int(input())
l=list(map(int,input().split()))
e=[i for i in l if i%2!=0]
o=[i for i in l if i%2==0]
print(len(o),len(e))