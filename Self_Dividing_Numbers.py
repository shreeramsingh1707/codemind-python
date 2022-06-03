def selfdivid(n):
    i=n
    flag=0
    if(n%10==0):
        return 0
    while n>0:
        dig=n%10
        if(i%dig!=0):
            flag=1
            break
        n//=10
    if flag==0:
        return 1
    else:
        return 0
    
a=int(input())
b=int(input())
for n in range(a,b+1):
    if(selfdivid(n)):
        print(n,end=" ")