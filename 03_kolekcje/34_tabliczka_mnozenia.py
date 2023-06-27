# 4▹ Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami
# mnożenia wiersz × kolumna.

tabliczka = [[(wiersz+1)*(kolumna+1) for kolumna in range(10)] for wiersz in range(10)]

# Wyświetlanie tabliczki mnożenia
for wiersz in tabliczka:
    for liczba in wiersz:
        print(liczba, end='\t')
    print()