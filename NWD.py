def nwd (a, b):

    while b:
        temp = a
        a = b
        b = temp%b
    return a

a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))

print("NWD(a, b) = " + str(nwd(a, b)))