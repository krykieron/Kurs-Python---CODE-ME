# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
# #
# #  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

bez_duplikatow = tuple(set(example_list))
minimum = min(bez_duplikatow)
maksimum = max(bez_duplikatow)

print(bez_duplikatow)
print("Minimalna liczba:", minimum)
print("Maksymalna liczba:", maksimum)