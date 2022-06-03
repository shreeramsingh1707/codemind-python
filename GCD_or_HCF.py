a,b=map(int,input().split())
if a<b:
    min=a
else:
    min=b
while(1):
    if a%min==0 and b%min==0:
        print(min)
        break
    min=min-1