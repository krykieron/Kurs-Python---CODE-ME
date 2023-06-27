# 2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
cena_benzyny = float(input('Jaka jest obecnie cena benzyny?'))
trasa = float(input('Podaj dystans do pokonania: '))
spalanie = float(input('Ile spala Twoje auto?'))
koszt_wyprawy = trasa * spalanie * cena_benzyny / 100
print('Całkowity koszt wyprawy wyniesie', round(koszt_wyprawy,2), 'złote')