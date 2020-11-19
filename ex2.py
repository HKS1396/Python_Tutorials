op=input("Enter the operation to perform i.e +,-,*,/\n")
v1=float(input("Enter first number\n"))
v2=float(input("Enter second number\n"))
if op=='+':
    if v1==56 and v2==9:
        print(77)
    elif v1==9 and v2==56:
        print(77)
    else:
        print(v1+v2)
elif op=='*':
    if v1==45 and v2==3:
        print(555)
    elif v1==3 and v2==45:
        print(555)
    else:
        print(v1*v2)
elif op=='/':
    if v1==56 and v2==6:
        print(4)
    else:
        print(v1/v2)
else:
    print(v1-v2)