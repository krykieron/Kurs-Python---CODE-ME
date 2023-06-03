def suma_for(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


print("Suma - for: ", suma_for(10))

def suma_while(n):
    s = 0
    while n > 0:
        s += n
        n = n - 1
    return s


print("Suma - while: ", suma_while(10))


def suma_rec(n):
    if n == 1:
        return 1
    else:
        return n + suma_rec(n-1)


print("Suma rekurencyjnie: ", suma_rec(10))
