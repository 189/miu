from base32_tiny import encode


def encode_bytes(s: bytes) -> str:
    return encode(s, variant="Crockford")




