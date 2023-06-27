import random

def losuj_cytat(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        cytaty = plik.readlines()

    cytat = random.choice(cytaty).strip()
    autor = random.choice(cytaty).strip()

    print("Quote of the day is:")
    print("*" * len(cytat))
    print(" " * ((len(cytat) - len(cytat.strip())) // 2) + cytat.strip())
    print("*" * len(cytat))
    print(autor)
    print()

def wyswietl_losowe_cytaty(nazwa_pliku, ilosc_cytatow):
    with open(nazwa_pliku, 'r') as plik:
        cytaty = plik.readlines()

    losowe_cytaty = random.sample(cytaty, ilosc_cytatow)

    print("Random quotes:")
    for cytat in losowe_cytaty:
        cytat = cytat.strip()
        autor = random.choice(cytaty).strip()
        print("*" * len(cytat))
        print(" " * ((len(cytat) - len(cytat.strip())) // 2) + cytat.strip())
        print("*" * len(cytat))
        print(autor)
        print()

# Pobieranie nazwy pliku od użytkownika
nazwa_pliku = input("Podaj nazwę pliku z cytatami: ")

# Losowanie i wyświetlanie cytatów
losuj_cytat(nazwa_pliku)
wyswietl_losowe_cytaty(nazwa_pliku, 3)