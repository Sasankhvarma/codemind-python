n=int(input())
l=list(map(int,input().split()))
lst=[]
c=n//2
for i in l:
    c-=1
    lst.append(i)
    if c==0:
        break
k=sum(l)-sum(lst)
print(k-sum(lst))