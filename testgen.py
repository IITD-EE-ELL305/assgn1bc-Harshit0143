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
    
L = [
"00000 1 0101 0101 0000 00 0000 0000 0001", 
"01111 1 0101 0000 0000 00 0100 0000 0100",
"01111 1 0101 0000 0000 00 1000 0000 0100", 
"01111 1 0000 0000 0000 00 0100 0000 0100", 
"01111 1 0000 0000 0000 00 1000 0000 0100", 
"00101 1 0000 0101 0000 00 0000 0000 1011", 
"10000 1 0000 0000 0000 00 0000 0011 0000", 
"10011 1 0000 0000 0000 00 0000 0011 0100",
"10000 1 0000 0000 0000 00 0000 0000 1000", 
"01111 1 0010 0000 0000 00 1000 0000 1000",
"00000 1 0101 0101 0000 00 0000 0000 0001", 
"00101 1 0000 0000 0000 00 0000 0000 0000", 
"10000 1 0000 0000 0011 11 1111 1110 0100",
"01110 1 0001 0000 0000 00 0100 0000 0000", 
"00101 1 0000 0001 0000 00 0000 0000 0000",
"10000 1 0000 0000 0000 00 0000 0000 1000", 
"01110 1 0010 0000 0000 00 0100 0000 1000", 
"10100 0 0000 0000 0000 00 0000 0000 0000",
"11111 0 0000 0000 0000 00 0000 0000 0000"


] 



convert_prog(L)

# python3 tired.py