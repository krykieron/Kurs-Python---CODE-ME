# Napisz program, który dla 10 kolejnych liczb naturalnych
# wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
# 1 -> 1
# 2 + 1 -> 3
# 3 + 3 -> 6
# 4 + 6 -> 10

sum_num = 0

for num in range(1, 11):
    sum_num += num # -> sum_num = sum_num + num
    print(sum_num)