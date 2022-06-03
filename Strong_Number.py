n=int(input())
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
temp=n
su=0
while n>0:
    r=n%10
    su=su+fact(r)
    n=n//10
if(su==temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")

    