l=int(input())
for i in range(int(input())):
    a,b=map(int,input().split())
    if a<l or b<l:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")