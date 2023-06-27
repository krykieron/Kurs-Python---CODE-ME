# 2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
L_test.append((6))
L_test.extend((8))
print(L_test)
#to wszystko zadziała tylko na liscie
# insert()
# remove()
# sort()

T_test = (1, 2, 3, 4)
T_test.append((6))
L_test.extend((8))
print(T_test)

S_test = {1, 2, 3, 4}
S_test.append((6))
L_test.extend((8))
print(S_test)