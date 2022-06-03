n=int(input())
s=n*n
su=0
su1=0
while n>0:
    r=n%10
    su=su*10+r
    n//=10
b=su*su
while b>0:
    r1=b%10
    su1=su1*10+r1
    b//=10
if s==su1:
    print("True")
else:
    print("False")