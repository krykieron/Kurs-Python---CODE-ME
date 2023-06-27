plansza = [['.','.','.'],
           ['.','.','.'],
           ['.','.','.']]


aktualny_gracz = 'X'

def wyswietl_plansze():
    print('  1   2   3')
    print('A ' + ' | '.join(plansza[0]))
    print('B ' + ' | '.join(plansza[1]))
    print('C ' + ' | '.join(plansza[2]))

def sprawdz_wygrana():
    for wiersz in plansza:
        if wiersz[0] == wiersz[1] == wiersz[2] != '.':
            return True

    for kolumna in range(3):
        if plansza[0][kolumna] == plansza[1][kolumna] == plansza[2][kolumna] != '.':
            return True

    if plansza[0][0] == plansza[1][1] == plansza[2][2] != '.':
        return True
    if plansza[0][2] == plansza[1][1] == plansza[2][0] != '.':
        return True

    return False

def gra_kolko_i_krzyzyk():
    global aktualny_gracz
    ilosc_ruchow = 0

    print("Gra w Kółko i Krzyżyk")

    gracz1 = input("Imię gracza 1: ")
    gracz2 = input("Imię gracza 2: ")

    while not sprawdz_wygrana() and ilosc_ruchow < 9:
        wyswietl_plansze()

        ruch = input(f"{aktualny_gracz}, podaj swój ruch (np. A1): ")
        wiersz = ord(ruch[0]) - ord('A')
        kolumna = int(ruch[1]) - 1

        if plansza[wiersz][kolumna] == '.':
            plansza[wiersz][kolumna] = aktualny_gracz
            ilosc_ruchow += 1
            if aktualny_gracz == 'X':
                aktualny_gracz = 'O'
            else:
                aktualny_gracz = 'X'
        else:
            print("To pole jest już zajęte! Spróbuj jeszcze raz.")

    wyswietl_plansze()

    if sprawdz_wygrana():
        print(f"Gratulacje! Wygrał {aktualny_gracz}!")
    else:
        print("Remis!")


gra_kolko_i_krzyzyk()
