def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

liczba1 = 24
liczba2 = 36

wynik = nwd(liczba1, liczba2)
print(f"NWD({liczba1}, {liczba2}) = {wynik}")