def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

n = int(input("Podaj liczbę naturalną (nie większą niż 8): "))

if n <= 8:
    print("Wyniki dla kolejnych liczb naturalnych od 0 do", n)
    for i in range(n+1):
        wynik = silnia(i)
        print(f"{i}! = {wynik}")
else:
    print("Błąd! Liczba jest większa niż 8!")
