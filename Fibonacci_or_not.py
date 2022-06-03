n=int(input())
a=1
b=0
c=a+b
if a==n or b==n:
    print(True)
while 1:
    if c>n:
        print(False)
        break
    if c==n:
        print(True)
        break
    if c<n:
        c=a+b
        a=b
        b=c

    
    