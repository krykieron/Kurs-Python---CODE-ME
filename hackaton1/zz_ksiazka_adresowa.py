<<<<<<< HEAD --- nie działa
# Program przechowujący danę kontaktowe znajomych/klientów.

ksiazka_adr = [
	['Anna','Nowak','666-111-333','anna.nowak@gmail.com'],
	['Jan','Kaczmarek','665-123-456','jan.kaczmarek@op.pl'],
	['Frodo','Baggins','234-654-098','shireishere@mordor.com'],
	['Joanna','Dzwonek','234-567-111','asiamar@op.pl']
]
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie.

#Zadania to:
wybor = input('Wpisz liczbę aby:\n'
		'(1) - wyświetlić książkę adresową\n'
		'(2) - dodać wpis do książki\n'
		'(3) - usunąć wpis z książki\n'
		'(4) - zakończyć pracę programu\n')

# Wyświetlenie wszystkich wpisów
if wybor == '1':
	for kolumna in ksiazka_adr:
		print(kolumna[0],'_',kolumna[1], '_', kolumna[2],'_',kolumna[3])
	quit()

# Stworzenie nowego wpisu (dane wczytywane z klawiatury)
if wybor == '2':
		uzupelnienie = input("Wpisz imię, nazwisko, numer telefonu i email który chcesz dodać:").split()
		new_record = [
			uzupelnienie[0],
			uzupelnienie[1],
			uzupelnienie[2],
			uzupelnienie[3],
		]
		ksiazka_adr.append(new_record)
for kolumna in ksiazka_adr:
	print(kolumna[0], kolumna[1], kolumna[2], kolumna[3])

# Usunięcie wpisu

if wybor == '3':
	for col in ksiazka_adr:
		# print(col[0], 'u', col[1], 'u', col[2], 'u', col[3]),
		usuniete = input("Przepisz pozycję do usunięcia")
		ksiazka_adr.remove()
	print(ksiazka_adr)

# Zakończenie
if wybor == '4':
	print('_')
=======
# Program przechowujący danę kontaktowe znajomych/klientów.

ksiazka_adr = [
	['Anna','Nowak','666-111-333','anna.nowak@gmail.com'],
	['Jan','Kaczmarek','665-123-456','jan.kaczmarek@op.pl'],
	['Frodo','Baggins','234-654-098','shireishere@mordor.com'],
	['Joanna','Dzwonek','234-567-111','asiamar@op.pl']
]
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie.

#Zadania to:
wybor = input('Wpisz liczbę aby:\n'
		'(1) - wyświetlić książkę adresową\n'
		'(2) - dodać wpis do książki\n'
		'(3) - usunąć wpis z książki\n'
		'(4) - zakończyć pracę programu\n')

# Wyświetlenie wszystkich wpisów
if wybor == '1':
	for kolumna in ksiazka_adr:
		print(kolumna[0],'_',kolumna[1], '_', kolumna[2],'_',kolumna[3])
	quit()

# Stworzenie nowego wpisu (dane wczytywane z klawiatury)
if wybor == '2':
		uzupelnienie = input("Wpisz imię, nazwisko, numer telefonu i email który chcesz dodać:").split()
		new_record = [
			uzupelnienie[0],
			uzupelnienie[1],
			uzupelnienie[2],
			uzupelnienie[3],
		]
		ksiazka_adr.append(new_record)
for kolumna in ksiazka_adr:
	print(kolumna[0], kolumna[1], kolumna[2], kolumna[3])

# Usunięcie wpisu

if wybor == '3':
	for col in ksiazka_adr:
		# print(col[0], 'u', col[1], 'u', col[2], 'u', col[3]),
		usuniete = input("Przepisz pozycję do usunięcia")
		ksiazka_adr.remove()
	print(ksiazka_adr)

# Zakończenie
if wybor == '4':
	print('_')
>>>>>>> origin/main
	quit()