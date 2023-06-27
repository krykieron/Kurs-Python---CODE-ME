def suma_wielokrotnosci(N):
    suma = 0
    for liczba in range(1, N):
        if liczba % 5 == 0 or liczba % 7 == 0:
            suma += liczba
    return suma

N = 21
wynik = suma_wielokrotnosci(N)
print(f"Suma wielokrotności 5 lub 7 poniżej {N} wynosi: {wynik}")