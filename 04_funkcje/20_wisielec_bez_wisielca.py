# 10▹ Stwórz grę wisielec “bez wisielca”.
# Możesz ograniczyć liczbę prób do np. 10.

import random

def gra_wisielec():
    wyrazy = ['python', 'programowanie', 'komputer', 'internet', 'ananas']
    wylosowany_wyraz = random.choice(wyrazy)
    dlugosc_wyrazu = len(wylosowany_wyraz)
    ukryty_wyraz = ['-'] * dlugosc_wyrazu
    zgadniete_litery = []
    liczba_prob = 10

    print("Zgadnij wylosowany wyraz. Masz 10 prób.")

    while liczba_prob > 0:
        print("Aktualny stan wyrazu: " + ' '.join(ukryty_wyraz))
        print("Zgadnij literę:")
        wprowadzona_litera = input().lower()

        if len(wprowadzona_litera) != 1:
            print("Wprowadź pojedynczą literę!")
            continue

        if wprowadzona_litera in zgadniete_litery:
            print("Ta litera została już zgadnięta. Spróbuj inną.")
            continue

        zgadniete_litery.append(wprowadzona_litera)

        if wprowadzona_litera in wylosowany_wyraz:
            print("Trafione!")
            for i in range(dlugosc_wyrazu):
                if wylosowany_wyraz[i] == wprowadzona_litera:
                    ukryty_wyraz[i] = wprowadzona_litera
        else:
            liczba_prob -= 1
            print("Nie trafione, spróbuj jeszcze raz! Pozostało prób:", liczba_prob)

        if '-' not in ukryty_wyraz:
            print("Brawo! Wygrałeś!, szukane to słowo to:", wylosowany_wyraz)
            break

    if liczba_prob == 0:
        print("Przegrałeś. Wylosowany wyraz to:", wylosowany_wyraz)

# Uruchomienie gry
gra_wisielec()
