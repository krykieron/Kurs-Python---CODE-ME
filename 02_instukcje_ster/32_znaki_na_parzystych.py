# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

#1
text = input("Podaj dowolny tekst: ")
result = ''

for i in range(len(text)):
    if i % 2 == 1:
        result += text[i]

print("Znaki na pozycjach parzystych:", result)
#2
text = input("Podaj dowolny tekst: ")
result = text[1::2]

print("Znaki na pozycjach parzystych:", result)