# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 (OK)
# i  zwróć łańcuch złożony z trzech środkowych znaków danego ciągu. (NIE :( )

wyraz = input('Podaj wyraz: ')
dlugosc = len(wyraz)

if dlugosc > 7 and dlugosc % 2 != 0 :
     print('Długość wyrazu jest nieparzysta i wynosi: ', dlugosc, '/n a jego środkowe liczby to')
else:
      print('Długość wyrazu jest parzysta i wynosi: ', dlugosc)

