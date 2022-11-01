n=int(input())
l=list(map(int,input().split()))
a=int(input())
lst=[]
for i in l:
    lst.append(i)
    a-=1
    if a==0:
        break
print(sum(lst))
