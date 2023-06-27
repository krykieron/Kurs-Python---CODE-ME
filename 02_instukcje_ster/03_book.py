# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

review1 = int(input('Book review 1 (1-10) -> '))
review2 = int(input('Book review 2 (1-10) -> '))
review3 = int(input('Book review 3 (1-10) -> '))

average = (review1 + review2 + review3)/3
average = round(average, 3)
print(average)

if average >= 7:
    print("very good")
elif average >= 4:
    print("not interesting")
else:
    print("bad")