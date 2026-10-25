with open('passwd.txt', 'r', encoding='utf-8') as file:
    password = file.read().strip()

with open('plain.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

allowed_chars = "abcdefghiklmnopqrstuvwxyz"

def generate_letters_from_password(password):
    password = password.lower().replace('j', 'i')
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    custom_letters = []

    for char in password:
        if char not in custom_letters and char in alphabet:
            custom_letters.append(char)

    for char in alphabet:
        if char not in custom_letters:
            custom_letters.append(char)

    return custom_letters

def prepare_input(input_text):
    input_text = input_text.lower().replace('j', 'i')

    input_text = ''.join([char for char in input_text if char in allowed_chars])

    result = ""
    i = 0
    while i < len(input_text):
        char1 = input_text[i]
        if i + 1 < len(input_text):
            char2 = input_text[i + 1]
            if char1 == char2:
                result += char1 + 'x'
                i += 1
            else:
                result += char1 + char2
                i += 2
        else:
            result += char1
            i += 1
    if len(result) % 2 != 0:
        result += 'x'
    return result

def split_into_pairs(input_text):
    pairs = []
    for i in range(0, len(input_text), 2):
        pairs.append(input_text[i: i + 2])
    return pairs

def encrypt(input_pairs):
    result = ''
    for pair in input_pairs:
        first_char = pair[0]
        second_char = pair[1]

        idx1 = letters.index(first_char)
        idx2 = letters.index(second_char)

        r1, c1 = idx1 // 5, idx1 % 5
        r2, c2 = idx2 // 5, idx2 % 5

        if r1 == r2:
            new_c1 = (c1 + 1) % 5
            new_c2 = (c2 + 1) % 5
            result += letters[r1 * 5 + new_c1] + letters[r2 * 5 + new_c2]

        elif c1 == c2:
            new_r1 = (r1 + 1) % 5
            new_r2 = (r2 + 1) % 5
            result += letters[new_r1 * 5 + c1] + letters[new_r2 * 5 + c2]

        else:
            result += letters[r1 * 5 + c2] + letters[r2 * 5 + c1]

    return result

def playfair(input):
    formatted_input = prepare_input(input)
    pairs_array = split_into_pairs(formatted_input)
    encrypted = encrypt(pairs_array)
    with open('substitute_proprietary.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted)

letters = generate_letters_from_password(password)
playfair(input_text)