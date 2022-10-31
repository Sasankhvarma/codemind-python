n=int(input())
l=map(int,str(n))
for i in l:
    if i%2!=0:
        print(i*i,end="")