a=int(input("enter the first number="))
b=int(input("enter the second number="))
while(b!=0):
    t=b
    b= a % b
    a=t
print(a)

