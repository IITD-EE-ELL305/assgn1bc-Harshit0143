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
    
L = ["10011 1 0000 0000 000000000000011000",
"10011 1 0000 0000 000000000000011000",
"10011 1 0000 0000 000000000000011000",
"00000 1 0001 0001 000000000000010011",
"00000 1 0010 0010 000000000000010111",
"11111 0 0000 0000 000000000000000000",
"00001 1 0001 0001 000000000000001010",
"00000 1 0010 0010 000000000000010100", 
"10100 0 0000 0000 000000000000000000"]

convert_prog(L)

# python3 tired.py