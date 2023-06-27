# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random

def gra_cieplo_zimno():
    liczba_do_zgadniecia = random.randint(1, 100)
    liczba_prob = 0
    zgadnieta = False

    print("Spróbuj zgadnąć liczbę od 1 do 100!")

    while not zgadnieta:
        liczba_prob += 1
        odpowiedz = int(input("Podaj swoją liczbę: "))

        if odpowiedz == liczba_do_zgadniecia:
            print("Zgadłeś!")
            zgadnieta = True
        elif odpowiedz < liczba_do_zgadniecia:
            print("Za mało!")
        else:
            print("Za dużo!")

    print(f"Gratulacje! Zgadłeś liczbę w {liczba_prob} próbach.")

gra_cieplo_zimno()