def przeszukiwanie_binarne(szukany_element, lista_elementow):
    lewy = 0
    prawy = len(lista_elementow) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2

        if lista_elementow[srodek] == szukany_element:
            return f"Number {szukany_element} is on the list"
        elif lista_elementow[srodek] < szukany_element:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return f"Number {szukany_element} is not on the list"


data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21

wynik = przeszukiwanie_binarne(elem, data)
print(wynik)
