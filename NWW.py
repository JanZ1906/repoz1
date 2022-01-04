def nww(a, b):
  if (a < b):
    return nww(b, a)
  k = a
  while (k % b != 0):
    k += a
  return k
a = int(input("Podaj liczby\n a = "))
b = int(input(" b = "));
print("NWW(a, b) = " + str(nww(a, b)))

