def max_of_2(x, y):
    return x if x > y else y
    # if x > y:
    #     return x
    # else:
    #     return y


def maximum_of_3(a, b, c):
    higher_value = max_of_2(a, b)
    return max_of_2(higher_value, c)

    # if a > b:
    #     return max_of_2(a, c)
    # else:
    #     return max_of_2(b, c)


# main
a = int(input("podaj liczbę nr 1-."))
b = int(input("podaj liczbę nr 2-."))
c = int(input("podaj liczbę nr 3 -."))
result = maximum_of_3(a, b, c)
print(result)