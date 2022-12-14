def encode(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decode(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def is_binary(text):
    for c in text:
        if (c != '1' and c != '0'):
            return False
    return True

def translate(text):
    if is_binary(text):
        return decode(text)
    else:
        return encode(text)
