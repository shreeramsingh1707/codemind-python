n=int(input())
su=0
temp=n
while su!=1 and su!=4:
    su=0
    while temp!=0:
        r=temp%10
        su=su+r*r
        temp=temp//10
    temp=su
if(su==1):
    print("True")
else:
    print("False")
