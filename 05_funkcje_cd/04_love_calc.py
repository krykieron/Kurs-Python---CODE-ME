def oblicz_dopasowanie(imie1, imie2):
    litery = {}
    for litera in imie1 + imie2 + "LOVE":
        litery[litera] = litery.get(litera, 0) + 1

    suma_wystapien = sum(litery.values())
    while suma_wystapien > 99:
        suma_wystapien = sum(int(cyfra) for cyfra in str(suma_wystapien))

    return suma_wystapien

def gra_wróżba():
    imie1 = input("Podaj imię pierwszej osoby: ")
    imie2 = input("Podaj imię drugiej osoby: ")

    dopasowanie = oblicz_dopasowanie(imie1.upper(), imie2.upper())

    print("Stopień dopasowania pary:")
    print(f"{dopasowanie}%")

# Uruchomienie gry
gra_wróżba()
