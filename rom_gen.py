#!/usr/bin/env python3


codes = {
'add' : ['00000', (False,True)],  
'sub' : ['00001', (False,True)],
'cmp' : ['00101', (False,True)],
'ld'  : ['01110', (True,)], 
'st'  : ['01111', (True,)],
'beq' : ['10000', (True,)],
'call': ['10011', (True,)],
'ret' : ['10100', (False,)],
'hlt' : ['11111', (False,)],
'and' : ['00110' , (False , True)],
'or'  : ['00111' , (False , True)],
'xor' : ['11110' , (False , True)],
}

def convert(binary_string , len_):
    decimal_value = int(binary_string, 2)
    hexadecimal_string = hex(decimal_value)[2:].zfill(len_)
    return hexadecimal_string
def little_endian(code):
    hex_pairs = [code[i:i+2] for i in range(0, len(code), 2)]
    hex_pairs.reverse()
    return   ' '.join(hex_pairs)

def pcVal(ops , isEq):
    higher = ops == 'ret' or ops == 'call'
    lower = ((isEq) and (ops == 'beq')) or (ops == 'ret')
    return bit_str(higher) + bit_str(lower)
def bit_str(bit):
    return '1' if bit else '0'  

def give_ALU_SEL(ops):
    if ops == 'sub':
        return "0001"
    elif ops == 'and':
        return "0010"
    elif ops == 'or':
        return '0011'
    elif ops == 'xor':
        return '0100'
    return '0000'

write_enable_cmds = ['ld' , 'add' , 'sub' , 'and' , 'or' , 'xor']
RegWEn = False
BSel = False
FlWEn = False
ALUSel = "0000"
WBSel = False
rs2Sel = False
ASel = False
PCSel = "00"
Wpc = False
hlt = False
ROM_LINES = dict()
for ops in codes:
    OP = codes[ops][0]
    for I in codes[ops][1]:
        for isEq in [False , True]:
            RegWEn = ops in write_enable_cmds  
            BSel = I
            FlWEn = ops == 'cmp'
            ALUSel = give_ALU_SEL(ops)
            WBSel = ops == 'ld'
            rs2Sel = ops == 'st'
            ASel = ops == 'beq'
            PCSel = pcVal(ops , isEq)
            Wpc = ops == 'call'
            hlt = ops == 'hlt'
            locn = OP + bit_str(I) + bit_str(isEq)
            data =  bit_str(RegWEn)+ \
                    bit_str(BSel)  + \
                    bit_str(FlWEn) + \
                    ALUSel         + \
                    bit_str(WBSel) + \
                    bit_str(rs2Sel)+ \
                    bit_str(ASel)  + \
                    PCSel          + \
                    bit_str(Wpc)   + \
                    bit_str(hlt)
            print('OP:' , ops)
            print("I:" , I)
            print("isEq:" , isEq)
            print(locn)
            print(data, '\n')
            locn = convert(locn , 2)
            data = convert(data , 4)
          
            # data = little_endian(data)
            line = locn + ': ' + data
            ROM_LINES[locn] = line
            

print('\n\nv3.0 hex words addressed')
for line_num in range(128):
    hex_id =  hex(line_num)[2:].zfill(2)
    if hex_id in ROM_LINES:
        print(ROM_LINES[hex_id])
    else:
        print(hex_id + ': 0000')
print('\n\n')
                