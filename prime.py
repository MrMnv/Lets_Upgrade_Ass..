n2=int(input(enter any number))
if n2 > 1:
    for i in range(2, n2//2):
        if(n2 % i) == 0:
            print(n2, "is NOT a Prime Number !")
            break
        else:
            print(n2, "is a Prime Number")
else:
    print(n2,"is NOT a Prime Number !")