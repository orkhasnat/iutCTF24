charmap = {
    'a': 'ﬧ',
    'b': 'コ',
    'c': '┘',
    'd': 'п',
    'e': 'ߛ',
    'f': 'ப',
    'g': '厂',
    'h': 'ⵎ',
    'i': 'ட',
    'j': 'ᒣ',
    'k': 'ᓗ',
    'l': 'ᒧ',
    'm': 'ᒉ',
    'n': 'ᑭ',
    'o': 'ᘂ',
    'p': 'ᒥ',
    'q': 'ᓕ',
    'r': 'ᒪ',
    's': 'ᒭ',
    't': 'ᓘ',
    'u': 'ᒨ',
    'v': 'ᒕ',
    'w': 'ᑮ',
    'x': 'ᒎ',
    'y': 'ᓟ',
    'z': 'ᓛ'
}

reverse_charmap = {value: key for key, value in charmap.items()}

text = "know your base sixty four"

encode = lambda st: "".join(
    [charmap[ch] if ch in charmap else ch for ch in st])
decode = lambda encoded: ''.join(
    [reverse_charmap[ch] if ch in reverse_charmap else ch for ch in encoded])

print(encode(text))