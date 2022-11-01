n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in l:
    if i%2==0:
        break
    lst.append(i)
print(sum(lst))