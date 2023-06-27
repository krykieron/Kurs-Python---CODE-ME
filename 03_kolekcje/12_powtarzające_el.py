# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

my_tuple = (1, 2, 3, 4, 3, 2, 5, 6, 4)

duplicates = set()
seen = set()

for element in my_tuple:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

print("Powtarzające się elementy w krotce to:", duplicates)