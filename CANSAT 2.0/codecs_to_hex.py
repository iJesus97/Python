import binascii


def to_hex(t, nbytes):
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    x = (hex_version[start:start + chars_per_item]
        for start in range(0, len(hex_version), chars_per_item)
    )
    return b' '.join(x)


if __name__ == '__main__':
    print(to_hex(b'abcdef', 1))
    print(to_hex(b'abcdef', 2))