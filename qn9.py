l=int(input("enter the limit="))
list=[]
for i in range(l):
    n = int(input("enter the numbers="))
    list.append(n)
for i in list:
    print("square=",pow(i,2))