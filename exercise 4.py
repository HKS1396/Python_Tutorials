n = int(input("Enter a number\n"))
c = int(input("Enter a choice 0 or 1\n"))
b = bool(c)
i = 1
if b == True:
    while i <= n:
        print(i * "*")
        i += 1
else:
    while n >= i:
        print(n * "*")
        n -= 1