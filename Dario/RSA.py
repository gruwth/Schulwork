def encode(message, e, n):
    return ','.join(str(pow(ord(c), e, n)) for c in message)

def decode(message, d, n):
    return ''.join(chr(pow(int(c), d, n)) for c in message.split(','))

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)

def main(message):
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    encoded = encode(message, *public)
    decoded = decode(encoded, *private)
    print(f"Public key: {public}\nPrivate key: {private}\nMessage: {message}\nEncoded: {encoded}\nDecoded: {decoded}")

if __name__ == "__main__":
    message = input("Enter message to encode/decode: ")
    main(message)