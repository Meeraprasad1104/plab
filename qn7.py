y=int(input("Enter the year="))
if y%100==0:
    if y%400==0:
        print(y,"leap year")
    else:
        print(y,"is not leap year")
else:
    if y%4==0:
        print(y, "leap year")
    else:
        print(y, "is not leap year")