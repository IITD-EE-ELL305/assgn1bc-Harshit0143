#!/usr/bin/env python3
# python3 tired.py
# 00000 0 0000 0000 0000 

# python3 tired.py


def convert(binary_string):
    binary_string = binary_string.replace(' ', '')
    decimal_value = int(binary_string, 2)
    hexadecimal_string = hex(decimal_value)[2:].zfill(8)
    hex_pairs = [hexadecimal_string[i:i+2] for i in range(0, len(hexadecimal_string), 2)]
    hex_pairs.reverse()
    return   ' '.join(hex_pairs)
  
def convert_prog(lis):
    print("\nv3.0 hex words addressed")
    for i in range(len(lis)):
        idx = hex(4 * i)[2:].zfill(3)
        print(f"{idx}: {convert(lis[i])}")
    print()
    
L = ["00000 1 0001 0001 000000000000010011",
"00000 1 0010 0010 000000000000010111",
"00001 1 0010 0010 000000000000000101",
"00110 0 0011 0001 001000000000000000",
"00110 1 0011 0011 000000000000000101",
"00111 0 0011 0001 001000000000000000",
"00111 1 0011 0011 000000000000000101",
"11110 0 0011 0001 001000000000000000",
"11110 1 0011 0011 000000000000000101"]

convert_prog(L)

# python3 tired.py