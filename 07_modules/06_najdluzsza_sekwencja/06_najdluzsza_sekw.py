def find_longest_sequence(text):
    longest_sequence = ""
    current_sequence = ""
    current_char = ""

    for char in text:
        if char == current_char:
            current_sequence += char
        else:
            current_char = char
            current_sequence = char

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence

    return longest_sequence, len(longest_sequence)

# Przykład użycia
var = str(input("wprowadz slowo:"))
longest_sequence, length = find_longest_sequence(var)
print(longest_sequence, length)