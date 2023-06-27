# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

Fahr = 0

while Fahr <= 200:
    celc = round(5 / 9 * (Fahr - 32), 2)
    print(f"temp {Fahr} F -> {celc} C")
    Fahr += 20

for Fahr in range(0, 201, 20):
    Celc = round(5/9 * (Fahr - 32), 2)
    print(f"{Fahr} stopni Fahrenheit = {Celc} stopni Celsiusza")