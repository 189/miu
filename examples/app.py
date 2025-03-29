from muzzy import base32_encode, base32_decode

message = base32_encode(b"f", "Crockford")

print(base32_decode(message, "Crockford").decode("utf-8"))


