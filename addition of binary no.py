def decimal():
    s=0
    x=0
    while(n!=0):
        r=n%10
        s=s+r**pow(2,x)
        n=n//10
        x+=1
def binary():
    s=' '
    while n!=0:
        r=n%2
        s=s+str(r)
        n=n//2

a=int(input("Enter the binary number:"))
b=int(input("Enter the second binary number:"))
c=decimal(a)+decimal(b)
print(c)
