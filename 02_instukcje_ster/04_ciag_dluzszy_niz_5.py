napis = input("Podaj tekst: ")

if len(napis) > 5 and 'a' in napis:
    nowy_napis = napis.replace('a', 'z')
    print("Zamieniony napis:", nowy_napis)
else:
    print("Nie spełniono warunków")