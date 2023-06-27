# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją
n = int(input('Podaj wielkosc matrycy 1-10:'))
tab = [['-'] * n] * n

for row in tab:
    print(' '.join(row))
