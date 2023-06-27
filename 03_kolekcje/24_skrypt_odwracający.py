#  Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]

input_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

if len(input_list) % 3 == 0:
    chunk_size = len(input_list) // 3 
    chunks = [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
    reversed_chunks = [chunk[::-1] for chunk in chunks]

    for chunk in reversed_chunks:
        print(chunk)
else:
     print("Podana lista nie ma długości podzielnej przez 3.")