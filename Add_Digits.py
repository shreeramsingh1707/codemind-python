
def  ad(n):
    su=0
    while n!=0:
        r=n%10
        su=su+r
        n//=10
    if su<10:
        return su
    else:
        return ad(su)
        
n=int(input())
print(ad(n))