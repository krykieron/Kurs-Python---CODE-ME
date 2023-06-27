# Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:

quote = 'Honesty is the first chapter in the book of wisdom.'
dlugosc = len(quote)
polowa = int(dlugosc / 2)

print('**Policz wszystkie znaki w napisie:\n', dlugosc)
print()
print('**Nie modyfikując zmiennej wyświetl słowo wisdom:\n', quote[-6:])
print()
print('**Wyświetl tylko pierwszą połowę tekstu:\n', quote[:polowa])
print()
print('**Wyświetl tylko kropkę:\n', quote[-1])
print()
print('**Wyświetl od połowy tylko co trzecią literę cytatu:\n', quote[polowa::3])
print()
print('**Wyświetl ‘Hnsyi h is hpe ntebo fwso.:\n', quote[::2])
print()
print('**Wyświetl cały cytat odwrotnie:\n', quote[::-1])
print()
print('**Zamień wisdom na słowo friendship:\n', quote.replace("wisdom", "friendship"))
print()
