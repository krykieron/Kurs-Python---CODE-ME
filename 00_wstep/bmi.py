wzrost = float(input('Podaj swój wzrost w metrach'))
waga = float(input('Podaj swoją wagę w kilogramach'))

BMI = waga / (wzrost ** 2)
print('Twoje BMI wynosi', round(BMI, 2))