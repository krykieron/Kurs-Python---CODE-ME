def znajdz_zwiazek(imie1, imie2):
    imie1 = imie1.lower()
    imie2 = imie2.lower()

    litery_imie1 = list(imie1)
    litery_imie2 = list(imie2)

    for litera in imie1:
        if litera in litery_imie2:
            litery_imie1.remove(litera)
            litery_imie2.remove(litera)

    liczba_pozostalych_liter = len(litery_imie1) + len(litery_imie2)
    zwiazek = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Sibling']

    while len(zwiazek) > 1:
        indeks = (liczba_pozostalych_liter - 1) % len(zwiazek)
        zwiazek.pop(indeks)

    return zwiazek[0]

def gra_flames():
    imie1 = input("Podaj imię pierwszej osoby: ")
    imie2 = input("Podaj imię drugiej osoby: ")

    zwiazek = znajdz_zwiazek(imie1, imie2)

    print("Związek między osobami:")
    print(zwiazek)

# Uruchomienie gry
gra_flames()
