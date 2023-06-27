def silnia_iteracyjnie(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

# Przykładowe użycie
n = 5
wynik_iteracyjnie = silnia_iteracyjnie(n)
print(f"Silnia z {n} (iteracyjnie): {wynik_iteracyjnie}")

# -----------------------------------------------------
def silnia_rekurencyjnie(n):
    if n == 0:
        return 1
    else:
        return n * silnia_rekurencyjnie(n - 1)

# Przykładowe użycie
n = 5
wynik_rekurencyjnie = silnia_rekurencyjnie(n)
print(f"Silnia z {n} (rekurencyjnie): {wynik_rekurencyjnie}")