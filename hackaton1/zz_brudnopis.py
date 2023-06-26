kontakty_i_numery = {'Anna Nowak': 444 333 222, 'Jan Kolasa': 111 222 333}

numery_i_kontakty = {}

for key, val in kontakty_i_numery.items():
    numery_i_kontakty[val] = key

wybór = input("Wyszukiwanie wg. numeru czy kontaktu?(Wpisz 'nr' lub 'k'): ")

if wybór == 'nr':
    numer = int(input("Podaj numer: "))
    print('Kontakt: ', numery_i_kontakty.get(numer))
else:
    kontakt = input("Podaj nazwę kontaktu: ")
    print('Numer: ', kontakty_i_numery.get(kontakt))