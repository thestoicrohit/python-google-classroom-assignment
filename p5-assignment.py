val = 0xCAFE
last_four = val & 0xF
count = bin(last_four).count('1')
if count >= 3:
    print(True)
else:
    print(False)
reversed_val = ((val & 0xFF) << 8) | ((val & 0xFF00) >> 8)
print(hex(reversed_val))
rotated = ((val & 0xF) << 12) | (val >> 4)
print(hex(rotated))
